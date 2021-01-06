<template>
  <div class="card">
    <div class="card-body">
      <input type="button" class="btn" id="test1" value="alert" @click="myfunc4(this)"/>
      <button class="btn" id="test2" value="koko" @click="myfunc3(this)">カウントUP</button>
      <!-- <input type="button" class="btn" id="test3" value="L2M" @click="myfunc2(this)"/>
      <input type="button" class="btn" id="test3" value="data input" @click="myfunc6(this)"/> -->
      <div button-okiba>
        ☆最大10連ランダムガチャ☆
        <input type="button" class="btn-null" value="null" @click="myfunc4(this)"/>
        <input type="button" class="btn-building" value="building" @click="myfunc4(this)"/>
        <input type="button" class="btn-Von-side" value="Von-side" @click="myfunc4(this)"/>
        <input type="button" class="btn-Voff-side" value="Voff-side" @click="myfunc4(this)"/>
        <input type="button" class="btn-Von-vertical" value="Von-vertical" @click="myfunc4(this)"/>
        <input type="button" class="btn-Voff-vertical" value="Voff-vertical" @click="myfunc4(this)"/>
      </div>
      <div test-table>
        <div table-header>
          <div column park-column>
            <div>駐車場test1-駐車場API⇒車両有無で色分け</div>
          </div>
        </div>
        <!-- <div class="ex-table-body">
          <form
            v-show="row.isShow"
            class="row use-park-row"
            v-for="(row, index) in useParkList"
            :key="index"
          >
            <div v-if="row.vehicle">
              <input
                type="button"
                class="btn3"
                v-model="row.park.parkName"
                :readonly="true"
              />
            </div>
            <div v-else>
              <input
                type="button"
                class="btn2"
                v-model="row.park.parkName"
                :readonly="true"
              />
            </div>
          </form>
        </div> -->
      </div>
      <div test-table>
        <div table-header>
          <div column park-column>
            <div>駐車場test2-2次元配列をv-forで表示</div>
          </div>
        </div>
        <!-- <div test-body>
          <span v-for="(item, index) in myarray1" :key="index">
            <div>
              <span v-for="(cell, index) in myarray1" :key="index">
                <input
                    v-show="cell"
                    type="button"
                    class="btn"
                    v-model="item[index]"
                />
              </span>
            </div>
          </span>
        </div> -->
      </div>
      <div test-table>
        <div table-header>
          <div column park-column>
            <div>駐車場test3-多次元連想配列をv-for,ifで表示</div>
          </div>
        </div>
        <!-- <div test-body>
          <span v-for="(item, index) in myarray2" :key="index">
            <div>
              <span v-for="(cell, index) in myarray2[index]" :key="index">
                <input
                    v-if="item[index].vehicleON"
                    type="button"
                    class="btn3"
                    v-model="item[index].parkID"
                />
                <input
                    v-else
                    type="button"
                    class="btn2"
                    v-model="item[index].parkID"
                />
              </span>
            </div>
          </span>
        </div> -->
      </div>
      <div test-table>
        <div table-header>
          <div column park-column>
            <div>駐車場test4-多次元連想配列にAPIぶちこんでv-for,ifで表示</div>
          </div>
        </div>
        <!-- <div test-body>
          <span v-for="(item, index) in myarray3" :key="index">
            <div>
              <span v-for="(cell, index) in myarray3[index]" :key="index">
                <input
                    v-if="item[index].vehicleON"
                    type="button"
                    class="btn"
                    v-model="item[index].parkName"
                    @click="openReturnPark(item[index].parkID)"
                />
                <input
                    v-else
                    type="button"
                    class="btn"
                    v-model="item[index].parkName"
                    @click="openSetVehicle(item[index].parkID)"
                />
              </span>
            </div>
          </span>
        </div> -->
      </div>
      <div test-table>
        <div table-header>
          <div column park-column>
            <div>駐車場test5-DBからmapをAPI=>データ格納して表示</div>
          </div>
        </div>
        <div test-body>
          <span v-for="(item, index) in myarray5" :key="index">
            <div>
              <span v-for="(cell, index) in myarray5[index]" :key="index">
                <input
                type="button"
                v-bind:class="item[index].btnClass"
                  :value="item[index].parkId"
                />
                <!-- <input
                    v-show="item[index].parkName === null && item[index].building === true"
                    type="button"
                    class="btn-building"
                />
                <input
                    v-show="item[index].parkName === null && item[index].building === false"
                    type="button"
                    class="btn-null"
                />
                <input
                    v-show="item[index].parkId && item[index].vehicleOn && item[index].btnDirection === true"
                    type="button"
                    class="btn-Von-side"
                    v-model="item[index].parkName"
                    @click="openReturnPark(item[index].parkId)"
                />
                <input
                    v-show="item[index].parkId && item[index].vehicleOn === null && item[index].btnDirection === true"
                    type="button"
                    class="btn-Voff-side"
                    v-model="item[index].parkName"
                    @click="openSetVehicle(item[index].parkId)"
                />
                <input
                    v-show="item[index].parkId && item[index].vehicleOn && item[index].btnDirection === false"
                    type="button"
                    class="btn-Von-vertical"
                    v-model="item[index].parkName"
                    @click="openReturnPark(item[index].parkId)"
                />
                <input
                    v-show="item[index].parkId && item[index].vehicleOn == null && item[index].btnDirection === false"
                    type="button"
                    class="btn-Voff-vertical"
                    v-model="item[index].parkName"
                    @click="openSetVehicle(item[index].parkId)"
                /> -->
              </span>
            </div>
          </span>
        </div>
      </div>
      <div>
        <Test></Test>
      </div>
      <div>
        <SetVehicle
        v-if="isOpenSetVehicle && selectedUseParkIndex != null"
        :selected-use-park="selectedUsePark"
        @set-vehicle-ok="setVehicleOk"
        @set-vehicle-cancel="setVehicleCancel"
      ></SetVehicle>
        <ReturnPark
        v-if="isOpenReturnPark && selectedUseParkIndex != null"
        :selected-use-park="selectedUsePark"
        :is-force="false"
        @return-park-ok="returnParkOk"
        @return-park-cancel="returnParkCancel"
      ></ReturnPark>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { Component, Prop, Vue, Watch } from "vue-property-decorator";
import Test from "../components/use-park/Test.vue";
import ParkDetail from "../components/master/ParkDetail.vue";
import SetVehicle from "../components/use-park/SetVehicle.vue";
import ReturnPark from "../components/use-park/ReturnPark.vue";
import { Root } from "../store/Root";
import { DecaManage } from "../store/deca/DecaManage";
import { VehicleManage } from "../store/master/VehicleManage";
import { ParkManage } from "../store/master/ParkManage";
import { UseParkManage } from "../store/use-park/UseParkManage";
import * as RootModel from "../models/model.root";
import * as MasterModel from "../models/master/model.master";
import * as UseParkModel from "../models/use-park/model.use-park";
import * as DecaModel from "../models/deca/model.deca";
import * as Const from "../const";
import moment from "moment";
import axios from 'axios';
import Converter from "../util/converter";
import { indexOf } from "lodash";

let apiTest = 0;
const url = "http://172.16.193.81:8081/vms" + "/api/api_test/v1/api_test" + "?" + moment();

@Component({
  components: { Test, SetVehicle, ReturnPark }
})
export default class SubMenus extends Vue {
  private horizontalAxisLeft: number = 0;
  private verticalAxisTop: number = 0;

  private searchParkName: string = "";
  private selectedUseParkIndex: number | null = null;
  private selectedUserNo: string | null = null;

  private isOpenUseHistory: boolean = false;
  private isOpenSetVehicle: boolean = false;
  private isOpenReturnPark: boolean = false;
  private isOpenForceReturnPark: boolean = false;

  private myarray1 = [
    [[1, 1], [2, 1], [3, 1]],
    [[1, 2], [2, 2], [3, 2]],
    [[1, 3], [2, 3], [3, 3]]
  ];

  private myarray2 = [
    [{addres: [1, 1], parkID: 1, vehicleON: true}, {addres: [1, 2], parkID: 2, vehicleON: true}],
    [{addres: [2, 1], parkID: 14, vehicleON: true}, {addres: [2, 2], parkID: 15, vehicleON: true}]
  ];

  private myarray3 = [
    [{addres: [1, 1], parkID: 1, parkName: "btn", vehicleON: 0, switch: true}],
    [{addres: [1, 2], parkID: 2, parkName: "btn-building", vehicleON: 0, switch: false}],
    [{addres: [1, 3], parkID: 3, parkName: "btn-Von-side", vehicleON: 0, switch: true}]
  ];

  // private myarray4: [[{
  //   id: number;
  //   addresX: number;
  //   addresY: number;
  //   parkId: number | null;
  //   parkName: string | null;
  //   vehicleOn: MasterModel.Vehicle | null;
  //   buildingOn: boolean;
  // }]];

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

  // beforeCreate() {
  //   console.log("beforeCreate");
  // }

  created() {
    console.log("created");
    this.initialize();
  }

  // beforeMount() {
  //   console.log("beforeMount");
  //   this.initialize();
  // }

  // mounted() {
  //   console.log("mounted");
  //   this.initialize();
  // }

  // beforeUpdate() {
  //   console.log("beforeUpdate");
  // }

  // updated() {
  //   console.log("updated");
  // }

  // beforeDestroy() {
  //   console.log("beforeDestroy");
  // }

  // destroyed() {
  //   console.log("destroyed");
  // }

  async initialize() {
    Root.SET_IS_LOADING(true);
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
    await this.myfunc2();
    await this.myfunc6();
    Root.SET_IS_LOADING(false);
  }

  async save() {
    Root.SET_IS_LOADING(true);
    for (const usePark of this.useParkList) {
      if (usePark.isAdd) {
        await UseParkManage.registUsePark(usePark).catch((err: any) => {
          Root.CONCAT_ERROR_LIST(err);
        });
      } else if (usePark.isChange) {
        await UseParkManage.updateUsePark(usePark).catch((err: any) => {
          Root.CONCAT_ERROR_LIST(err);
        });
      }
    }
    Root.SET_IS_LOADING(false);
    this.initialize();
  }

  reload() {
  this.initialize();
  }

  get vehicleList(): MasterModel.Vehicle[] {
    return VehicleManage.vehicleList;
  }

  get parkList(): MasterModel.Park[] {
    const parkList: MasterModel.Park[] = ParkManage.parkList;
    this.filterList(parkList);
    return parkList;
  }

  get useParkList(): UseParkModel.UsePark[] {
    const today = moment();
    const useParkList: UseParkModel.UsePark[] = [];
    // 駐車場の一覧が基準（使用駐車場の一覧ではなく）
    this.parkList.forEach((park: MasterModel.Park) => {
      const targetUsePark: UseParkModel.UsePark = UseParkManage.useParkList.find(
        (usePark: UseParkModel.UsePark) =>
          usePark.parkId === park.parkId &&
          usePark.status === Const.USE_PARK_STATUS.USING_VEHICLE
      ) || {
        useParkId: 0,
        parkId: park.parkId,
        vehicleId: null,
        startDate: null,
        endDate: null,
        status: null,
        notes: null,
        lastUpdateDate: "",
        lastUpdateUserNo: "",
        version: 0,
        isAlertReturnExpire: false,
        isReturnExpire: false,
        isAlertUseExpire: false,
        isUseExpire: false,
        isLeave: false,
        isShow: true,
        isDelete: false,
        isAdd: false,
        isChange: false,
        park: null,
        vehicle: null
      };
      // 対象の駐車場をセット
      targetUsePark.park = park;
      // 対象の車両をセット
      targetUsePark.vehicle =
        this.vehicleList.find(
          (vehicle: MasterModel.Vehicle) =>
            vehicle.vehicleId === targetUsePark.vehicleId
        ) || null;
      if (targetUsePark.vehicle !== null) {
        const diffReturnDays = moment(
          targetUsePark.vehicle.planReturnDate || ""
        ).diff(today, "days");
        const diffUseDays = moment(targetUsePark.vehicle.useEndDate || "").diff(
          today,
          "days"
        );
        targetUsePark.isReturnExpire = diffReturnDays < 0;
        if (!targetUsePark.isReturnExpire) {
          targetUsePark.isAlertReturnExpire = diffReturnDays < 7;
        }
        targetUsePark.isUseExpire = diffUseDays < 0;
        if (!targetUsePark.isUseExpire) {
          targetUsePark.isAlertUseExpire = diffUseDays < 7;
        }
      }
      // 放置
      const difflastDays = moment(targetUsePark.lastUpdateDate || "").diff(
        today,
        "days"
      );
      targetUsePark.isLeave = difflastDays < -30;

      useParkList.push(targetUsePark);
    });
    return useParkList;
  }

  get selectedUsePark(): UseParkModel.UsePark | null {
    // console.log("selected = " + this.useParkList[this.selectedUseParkIndex].parkId);
    return this.selectedUseParkIndex != null
      ? JSON.parse(JSON.stringify(this.useParkList[this.selectedUseParkIndex]))
      : null;
  }

  get mapLists(): DecaModel.ParkMap[] {
    return DecaManage.mapLists;
  }

  onScrollTable(evt: any) {
    this.horizontalAxisLeft = 0 - evt.target.scrollLeft;
    this.verticalAxisTop = 0 - evt.target.scrollTop;
  }

  filterList(parkList: MasterModel.Park[]) {
    parkList.forEach((park: MasterModel.Park) => {
      if (park.isAdd) {
        park.isShow = true;
      } else {
        park.isShow = park.parkName.indexOf(this.searchParkName) !== -1;
      }
    });
  }

  openSetVehicle(parkID: number | null) {
    this.useParkList.some((useParkList, index) => {
      if (useParkList.parkId === parkID) {
        this.selectedUseParkIndex = index;
        return true;
      }
    });
    this.isOpenSetVehicle = true;
    console.log("index =" + this.selectedUseParkIndex);
  }

  setVehicleOk(usePark: UseParkModel.UsePark) {
    if (this.selectedUseParkIndex != null) {
      usePark.isAdd = true;
      usePark.startDate = moment().format("YYYY-MM-DD HH:mm:ss");
      usePark.status = Const.USE_PARK_STATUS.USING_VEHICLE;
      this.useParkList[this.selectedUseParkIndex] = usePark;
    }
    this.selectedUseParkIndex = null;
    this.isOpenSetVehicle = false;
    this.save();
  }

  setVehicleCancel() {
    this.selectedUseParkIndex = null;
    this.isOpenSetVehicle = false;
  }

  openReturnPark(parkID: number) {
    this.useParkList.some((useParkList, index) => {
      if (useParkList.parkId === parkID) {
        this.selectedUseParkIndex = index;
        return true;
      }
    });
    this.isOpenReturnPark = true;
    console.log("index =" + this.selectedUseParkIndex);
  }

  returnParkOk(usePark: UseParkModel.UsePark) {
    if (this.selectedUseParkIndex != null) {
      usePark.isChange = true;
      usePark.endDate = moment().format("YYYY-MM-DD HH:mm:ss");
      usePark.status = Const.USE_PARK_STATUS.RETURN;
      this.useParkList[this.selectedUseParkIndex] = usePark;
    }
    this.selectedUseParkIndex = null;
    this.isOpenReturnPark = false;
    this.save();
  }

  returnParkCancel() {
    this.selectedUseParkIndex = null;
    this.isOpenReturnPark = false;
  }

  myfunc1() {
    const a = "わっしょい";
    console.log(a);
    return a;
  }

  myfunc2() {
    let tmp = 0;
    let array = [];
    const rtn = [];
    // console.log("mapLists");
    // console.log(this.mapLists)
    for (let i = 0; i < 5; i++) {
      array = [];
      for (let j = 0; j < 5; j++) {
        tmp = (i * 5) + j;
        array.push(this.mapLists[tmp]);
        // array[j]("btnClass");
      }
      rtn.push(array);
    }
    console.log(rtn);
    this.myarray5 = rtn;
    // console.log("D2M end");
    // console.log(this.myarray5);
  }

  myfunc3() {
    const gaba1 = document.getElementById("test2") as HTMLInputElement;
    const aaa = ++apiTest;
    const bbb = String(aaa);
    console.log(bbb);
    gaba1.innerHTML = bbb;
  }

  myfunc4() {
    const item = ['☆1 skkbr', '☆1 yasuda', '☆1 ota', '☆1 yuki', '☆1 aidoru', '☆2 sakamoto', '☆2 takahasi', '☆2 higasi', '☆2 ', '☆2', '☆3', '☆3', '☆3', '☆3', '☆4', '☆4', '☆5'];
    const rnd = Math.floor(Math.random() * 10);
    for (let i = 0; i < rnd; i++) {
      alert(item[Math.floor(Math.random() * item.length)]);
    }
  }

  // とりあえずの激重script 30*30*200=180*10^3
  // myfunc5() {
  //   for (let i in this.myarray3) {
  //     for (let j in this.myarray3[i]) {
  //       this.useParkList.forEach((useParkList) => {
  //         if (this.myarray3[i][j].parkID === useParkList.parkId) {
  //           this.myarray3[i][j].parkName = useParkList.park.parkName;
  //           this.myarray3[i][j].vehicleON = useParkList.vehicle;
  //         }
  //       });
  //     }
  //   }
    // console.log(this.myarray3);
  // }

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
        // console.log(this.myarray4[i][j].parkId, this.useParkList[tmp].parkId);
      }
    }
    // console.log("I2M end");
    // console.log(this.myarray5);
  }

  onChange(park: MasterModel.Park) {
    if (!park.isAdd) {
      park.isChange = true;
    }
  }

}

</script>

<style scoped lang="scss">
.park-ex-table {
  height: calc(100vh - 100px);
}

.park-row {
  height: 30px;
}

.park-column,
.park-row {
  > div {
    min-width: 100px;
    max-width: 100px;
    &:nth-of-type(1) {
      min-width: 40px;
      max-width: 40px;
    }
    &:nth-of-type(3) {
      min-width: 110px;
      max-width: 110px;
    }
    &:nth-of-type(4) {
      min-width: 200px;
      max-width: 200px;
    }
    &:nth-of-type(5),
    &:nth-of-type(6),
    &:nth-of-type(7) {
      min-width: 90px;
      max-width: 90px;
    }
    &:nth-of-type(8) {
      min-width: 200px;
      max-width: 200px;
    }
    &:nth-last-of-type(3) {
      min-width: 90px;
      max-width: 90px;
    }
    &:nth-last-of-type(2) {
      min-width: 70px;
      max-width: 70px;
    }
    &:nth-last-of-type(1) {
      min-width: 60px;
      max-width: 60px;
    }
  }
}
</style>
