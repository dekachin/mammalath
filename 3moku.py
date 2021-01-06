<template>
  <div test-table>
    <div table-header>
      <div column park-column>
        <div>駐車場test5-DBからmapをAPI=>データ格納して表示</div>
      </div>
    </div>
    <div test-body>
      // v-forでmuarray5の縦*横の長さだけボタンを表示させる
      <span v-for="(item, index) in myarray5" :key="index">
        <div>
          <span v-for="(cell, index) in myarray5[index]" :key="index">
            // ボタンのclassはmyarray5の'btnclass'でバインドする
            <input
              type="button"
              v-bind:class="item[index].btnClass"
                :value="item[index].parkId"
            />
          </span>
        </div>
      </span>
    </div>
  </div>
</template>

<script lang="ts">
@Component({})
export default class SubMenus extends Vue {

　// myarray5は最初は空で定義
  private myarray5: [[{
    id: number;
    addresX: number;
    addresY: number;
    parkId: number | null;
    parkName: string | null;
    vehicleOn: MasterModel.Vehicle | null;
    building: boolean;
    btnDirection: boolean;
    btnClass: string | null;
  }]];

  // createdのタイミングで初期化(APIとか)を実施
  created() {
    this.initialize();
  }

  async initialize() {
    // load処理
    Root.SET_IS_LOADING(true);
    // promise.allでapiたたく
    await Promise.all([
      VehicleManage.loadVehicleList(),
      ParkManage.loadParkList(),
      UseParkManage.loadUseParkList(),
      DecaManage.loadMapLists()
      // this.myfunc2(),
      // this.myfunc6()
    ]).catch((err: any) => {
      Root.CONCAT_ERROR_LIST(err);
    });
    // apiでデータ持ってきてから処理を実施
    await this.myfunc2(); // 駐車場データを2次元配列に変換
    await this.myfunc6(); // 駐車場データと他データを合体させて'btn-class'をセット
    Root.SET_IS_LOADING(false);
  }

  myfunc2() {
    let tmp = 0;
    let array = [];
    const rtn = [];
    for (let i = 0; i < 5; i++) {
      array = [];
      for (let j = 0; j < 5; j++) {
        tmp = (i * 5) + j;
        array.push(this.mapLists[tmp]);
      }
      rtn.push(array);
    }
    console.log(rtn);
    this.myarray5 = rtn;
  }

  myfunc6() {
    let tmp = 0;
    for (let i = 0; i < this.myarray5.length; i++) {
      for (let j = 0; j < this.myarray5[i].length; j++) {
        tmp = (i * this.myarray5[i].length) + j;
        this.useParkList.forEach((useParkList) => {
          if (this.myarray5[i][j].parkId === useParkList.parkId) {
            this.myarray5[i][j].parkName = useParkList.park.parkName;
            this.myarray5[i][j].vehicleOn = useParkList.vehicle;
          }
          // btnClassをset
          if (this.myarray5[i][j].building === false) {
            this.myarray5[i][j].btnClass = "btn-null";
          } else {
            if (this.myarray5[i][j].parkId === null) {
              this.myarray5[i][j].btnClass = "btn-building";
            } else {
              if (this.myarray5[i][j].btnDirection === false) {
                if (this.myarray5[i][j].vehicleOn === null) {
                  this.myarray5[i][j].btnClass = "btn-Voff-vertical";
                } else {
                  this.myarray5[i][j].btnClass = "btn-Von-vertical";
                }
              } else {
                if (this.myarray5[i][j].vehicleOn === null) {
                  this.myarray5[i][j].btnClass = "btn-Voff-side";
                } else {
                  this.myarray5[i][j].btnClass = "btn-Von-side";
                }
              }
            }
          }
        });
      }
    }
  }

}
</script>
