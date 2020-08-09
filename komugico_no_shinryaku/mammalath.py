import random
from enum import IntEnum

# 動物定義
class Animal(IntEnum):
    EMPTY = 0
    RED = 1
    YLW = 2
    BLE = 3
    GRN = 4
    ORG = 5
    PPL = 6
    
    def __str__(self):
        """ 文字列定義

        Returns:
            str: 各値に割り振られた文字列
        """
        if self.value == Animal.EMPTY:
            return "　"
        if self.value == Animal.RED:
            return "１"
        if self.value == Animal.YLW:
            return "２"
        if self.value == Animal.BLE:
            return "３"
        if self.value == Animal.GRN:
            return "４"
        if self.value == Animal.ORG:
            return "５"
        if self.value == Animal.PPL:
            return "６"
    
    @staticmethod
    def animal_list():
        """ 動物リストの提供関数

        Returns:
            list[Animal]: 動物リスト
        """
        return [
            Animal(Animal.RED),
            Animal(Animal.YLW),
            Animal(Animal.BLE),
            Animal(Animal.GRN),
            Animal(Animal.ORG),
            Animal(Animal.PPL),
        ]

# 石定義
class Stone(IntEnum):
    EMPTY = 0
    PLAYER1 = 1
    PLAYER2 = 2

    def __str__(self):
        """ 文字列定義

        Returns:
            str: 各値に割り振られた文字列
        """
        if self.value == Stone.EMPTY:
            return "・"
        if self.value == Stone.PLAYER1:
            return "★"
        if self.value == Stone.PLAYER2:
            return "☆"

# ゲーム管理クラス
class Mammalath(object):
    # 走査方向定義
    VEC = [
        # dx, dy
        (0, -1),    # 上
        (1, -1),    # 右上
        (1, 0),     # 右
        (1, 1),     # 右下
        (0, 1),     # 下
        (-1, 1),    # 左下
        (-1, 0),    # 左
        (-1, -1)    # 左上
    ]

    # モード定義
    MODE_PUT_STONE = 1                  # モード：石を置く
    MODE_REMOVE_3_ANIMALS = 2           # モード：3頭開放
    MODE_REMOVE_SPECIFIC_ANIMAL = 3     # モード：1種開放
    MODE_TURN_EXCHANGE = 4              # モード：手番入れ替え

    def __init__(self):
        """ 初期化関数
        """
        self._board = Board()
        self._player = Stone.PLAYER1
        self._is_game_end = False
        self._turn = 1

    @property
    def is_game_end(self):
        return self._is_game_end
    
    def turn(self):
        """ ターン制御関数
        """
        # ターン表示
        print()
        print("TURN         >>> " + str(self._turn))
        print("NEXT PLAYER  >>> " + str(self._player))

        # 盤面表示
        self._board.show_cells()

        # 操作処理
        success = self.user_operation()
        
        # 走査の成功判定
        if success:
            # 終了判定
            self.judge_game_end()
            # ターン更新
            self._turn = self._turn + 1
            # 手番入れ替え
            if self._player == Stone.PLAYER1:
                self._player = Stone.PLAYER2
            else:
                self._player = Stone.PLAYER1
        else:
            # 操作失敗
            print("\t>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
            print("\t>>>>>>>>>>>>>>>>>>>>> FAILED!! <<<<<<<<<<<<<<<<<<<<<<<<<<")
            print("\t>>>>>>>>>>>>>>>>>>> TRY AGAIN!! <<<<<<<<<<<<<<<<<<<<<<<<<")
            print("\t>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")

    def user_operation(self):
        """ ユーザー操作関数

        Returns:
            bool: 操作の成否判定
        """
        # 成否判定フラグ
        success = False

        # モード選択
        stone = self._player
        if self._turn == 2:
            # 2ターン目のみ手番交換を表示
            print("SELECT MODE  >>>  1: Put stone, 2; Remove 3 animals, 3: Remove specific animal, 4: Exchange turn")
        else:
            print("SELECT MODE  >>>  1: Put stone, 2; Remove 3 animals, 3: Remove specific animal")
        mode = int(input())

        # 石置き
        if mode == self.MODE_PUT_STONE:
            print("SELECT POS   >>> x:1-6, y:1-6")
            x, y = map(int, input().split())
            success = self.put_stone(x-1, y-1, stone)

        # 3頭開放
        if mode == Mammalath.MODE_REMOVE_3_ANIMALS:
            print("SELECT POS   >>> x:1-6, y:1-6")
            x, y = map(int, input().split())
            print("SELECT DIR   >>> ↑:1, ↗:2, →:3, ↘:4, ↓:5, ↙:6, ←:7, ↖:8")
            idx = int(input())
            success = self.remove_3_animals(x-1, y-1, Mammalath.VEC[idx-1])

        # 1種開放
        if mode == Mammalath.MODE_REMOVE_SPECIFIC_ANIMAL:
            print("SELECT ANIMAL >>> animal:1-6")
            idx = int(input())
            if idx >= 1 and idx <=6:
                animal = Animal(idx)
                success = self.remove_specific_animal(animal)
            else:
                success = False
        
        # 手番交換
        if mode == Mammalath.MODE_TURN_EXCHANGE:
            if self._turn == 2:
                success = self.turn_exchange()
            else:
                success = False

        # 成功判定
        return success
    
    def put_stone(self, x, y, stone):
        """ 石を置く関数

        Args:
            x (int): X座標 0 - 5
            y (int): Y座標 0 - 5
            stone (Stone): 石 Stone.PLAYER1 or Stone.PLAYER2

        Returns:
            bool: 石を置けたかどうか
        """
        if self._board.put_stone(x, y, stone):
            # 石を置けた場合
            return True
        else:
            # 石を置けなかった場合
            return False

    def remove_3_animals(self, x, y, vec):
        """ 3頭開放関数

        Args:
            x (int): X座標 0 - 5
            y (int): Y座標 0 - 5
            vec ([int, int]): 操作方向ベクトル

        Returns:
            bool: 開放の成否判定
        """
        if self._board.exists_3_animals(x, y, vec):
            # 動物がすべてのマスに存在する場合，開放を実行
            self._board.remove_3_animals(x, y, vec)
            return True
        else:
            # 動物が存在しないマスがある場合，開放しない
            return False

    def remove_specific_animal(self, animal):
        """ 1種開放関数

        Args:
            animal (Animal): 開放対象の動物

        Returns:
            bool: 開放の成否判定
        """
        # 開放対象の動物の座標リストを取得
        positions = self._board.find_pos_specific_animal(animal)
        if len(positions) > 0:
            # 開放対象の動物が1頭でもいる場合
            for pos in positions:
                # 各座標の動物を開放
                self._board.remove_animal(pos[0], pos[1])
            return True
        else:
            # 開放対象の動物が1頭もいない場合
            return False
    
    def turn_exchange(self):
        """ 手番交換関数
        
        Returns:
            bool: 手番交換の成否判定
        """
        positions = self._board.get_pos_stone(Stone.PLAYER1)
        if len(positions) == 1:
            pos = positions[0]
            self._board.put_stone(pos[0], pos[1], Stone.PLAYER2, force=True)
            return True
        else:
            return False

    def judge_game_end(self):
        """ ゲームの終了判定
        """
        winner = None
        if self._board.judge_lose(self._player):
            # 敗北条件が成立
            self._is_game_end = True
            if self._player == Stone.PLAYER1:
                winner = Stone.PLAYER2
            else:
                winner = Stone.PLAYER1
        else:
            # 敗北条件が非成立
            if self._board.judge_win(self._player):
                # 勝利条件が成立
                self._is_game_end = True
                winner = self._player
            else:
                # 勝利も敗北も非成立
                return
        # ゲーム終了
        print()
        self._board.show_cells()
        print()
        print("\t>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
        print("\t>>>>>>>>>>>>>>>>>>>>> GAME END!! <<<<<<<<<<<<<<<<<<<<<<<<")
        print("\t>>>>>>>>>>>>>>>>>>> WINNER: " + str(winner) +"  <<<<<<<<<<<<<<<<<<<<<<<<<<")
        print("\t>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")

# 盤管理クラス
class Board(object):
    # 勝利・敗北判定用方向定義リスト
    JUDGE_CONDITIONS = [
        {"start": (0, 0), "end": (4, 6), "vec": (1, 0)},    # →
        {"start": (0, 0), "end": (6, 4), "vec": (0, 1)},    # ↓
        {"start": (0, 0), "end": (4, 4), "vec": (1, 1)},    # ↘
        {"start": (2, 0), "end": (6, 4), "vec": (-1, 1)},   # ↙
    ]

    def __init__(self):
        """ 初期化関数
        """
        self._cells = Board.get_init_cells()
    
    @staticmethod
    def get_init_cells():
        """ 初期盤面作成関数

        Returns:
            [[Cell]]: 初期盤面
        """
        # 2次元配列の空盤面作成
        cells = [[None for _ in range(6)] for _ in range(6)]
        # 6種x6頭の動物の空マス作成
        random_cells = [Cell(animal, Stone.EMPTY) for _ in range(6) for animal in Animal.animal_list()]
        # ランダムに混ぜる
        random.shuffle(random_cells)
        # 2次元配列の盤面に格納
        for y in range(6):
            for x in range(6):
                cells[y][x] = random_cells[x + y * 6]
        # 盤面返却
        return cells

    def show_cells(self):
        """ 盤面表示関数
        """
        print("\t+=======================================================+")
        for y in range(6):
            print("\t|", end="\t")
            for x in range(6):
                cell = self._cells[y][x]
                print(str(cell.animal) + "-" + str(cell.stone), end="\t")
            print("|", end="\n")
        print("\t+=======================================================+")
    
    def get_pos_stone(self, stone):
        """ 特定プレイヤーの石の位置を取得

        Args:
            stone (Stone): プレイヤー情報
        
        Returns:
            list[[int, int]]: 石の座標リスト
        """
        # 空の座標リスト
        positions = []
        for y in range(6):
            for x in range(6):
                cell = self._cells[y][x]
                if cell.stone == stone:
                    positions.append([x, y])
        return positions

    def put_stone(self, x, y, stone, force=False):
        """ 石を置く関数

        Args:
            x (int): X座標 0 - 5
            y (int): Y座標 0 - 5
            stone (Stone): 石 Stone.PLAYER1 or Stone.PLAYER2

        Returns:
            bool: 石を置けたかどうかの成否判定
        """
        if x >= 0 and x < 6 and y >= 0 and y < 6:
            # 座標が盤内の場合
            if self._cells[y][x].is_stone_empty():
                # 石がない場合，石を置く
                self._cells[y][x].put_stone(stone)
                return True
            else:
                # 石があった場合
                if force:
                    # 強制配置処理の場合（手番交換専用）
                    self._cells[y][x].put_stone(stone)
                    return True
                else:
                    # 通常処理の場合
                    return False
        else:
            # 座標が盤外の場合
            return False

    def exists_3_animals(self, x, y, vec):
        """ 3頭開放用の動物存在チェック関数

        Args:
            x (int): X座標 0 - 5
            y (int): Y座標 0 - 5
            vec ([int, int]): 操作方向ベクトル

        Returns:
            bool: 存在の成否判定（True: すべて存在, False：エラー）
        """
        for d in range(3):
            # 座標計算
            px = x + vec[0] * d
            py = y + vec[1] * d
            if px >= 0 and px < 6 and py >= 0 and py < 6:
                if self._cells[py][px].is_animal_empty():
                    # 空だった場合
                    return False
                else:
                    # 動物がいた場合
                    continue
            else:
                # 番外に出た場合
                return False
        # すべての走査マスに動物がいた場合
        return True

    def remove_3_animals(self, x, y, vec):
        """ 3頭開放関数

        Args:
            x (int): X座標 0 - 5
            y (int): Y座標 0 - 5
            vec ([int, int]): 操作方向ベクトル
        """
        for d in range(3):
            # 座標計算
            px = x + vec[0] * d
            py = y + vec[1] * d
            # 動物開放
            self.remove_animal(px, py)

    def remove_animal(self, x, y):
        """ 動物開放関数

        Args:
            x (int): X座標 0 - 5
            y (int): Y座標 0 - 5
        """
        self._cells[y][x].remove_animal()

    def find_pos_specific_animal(self, animal):
        """ 1種開放用の動物位置検索関数

        Args:
            animal (Animal): 開放対象の動物

        Returns:
            list[[int, int]]: 動物の座標リスト
        """
        # 空の座標リスト作成
        positions = []
        for y in range(6):
            for x in range(6):
                if self._cells[y][x].animal == animal:
                    # 動物が検索対象と一致した場合，リストに座標を追加
                    positions.append([x, y])
        # 座標リスト返却
        return positions
    
    def judge_lose(self, stone):
        """ 敗北判定

        Args:
            stone (Stone): プレイヤー情報

        Returns:
            bool: 敗北状況（True: 敗北, False: 敗北ではない）
        """
        judge_board = self.__convert_to_judge_board(stone)
        for judge_condition in Board.JUDGE_CONDITIONS:
            (start_x, start_y) = judge_condition["start"]
            (end_x, end_y) = judge_condition["end"]
            (dx, dy) = judge_condition["vec"]
            for y in range(start_y, end_y):
                for x in range(start_x, end_x):
                    sum = 0
                    for d in range(3):
                        sum = sum + judge_board[y + d * dy][x + d * dx]
                    if sum == 3 or sum == 6 or sum == 9:
                        # 敗北条件が成立
                        return True
                    else:
                        # 敗北条件が非成立
                        continue
        # 敗北条件がすべて非成立
        return False

    
    def judge_win(self, stone):
        """ 勝利判定

        Args:
            stone (Stone): プレイヤー情報

        Returns:
            bool: 勝利判定（True: 勝利, False: 勝利ではない）
        """
        judge_board = self.__convert_to_judge_board(stone)
        for judge_condition in Board.JUDGE_CONDITIONS:
            (start_x, start_y) = judge_condition["start"]
            (end_x, end_y) = judge_condition["end"]
            (dx, dy) = judge_condition["vec"]
            for y in range(start_y, end_y):
                for x in range(start_x, end_x):
                    sum = 0
                    for d in range(3):
                        sum = sum + judge_board[y + d * dy][x + d * dx]
                    if sum == 0:
                        # 勝利条件が成立
                        return True
                    else:
                        # 勝利条件が非成立
                        continue
        # 勝利条件がすべて非成立
        return False

    def __convert_to_judge_board(self, stone):
        """ 敗北，勝利判定用

        数値定義を
            -1  石なし
            0   石あり・開放済み
            3   石あり・未開放
        とすると，連続した3マスを加算したときに
            0        【勝利】すべて石あり・すべて解放済み
            3,6,9    【敗北】すべて石あり・未開放が混ざっている
            上記以外 【なし】石なしが含まれる
        となり，勝利と敗北の判定ができるので，上記定義に基づいて変換を行う．

        Args:
            stone (Stone): プレイヤー情報

        Returns:
            [[int]]: 判定用配列（-1: 石なし，0:石あり・解放済み, 3:石あり・未開放）
        """
        # 空の配列作成
        judge_board = [[None for _ in range(6)] for _ in range(6)]
        for y in range(6):
            for x in range(6):
                if self._cells[y][x].stone == stone:
                    if self._cells[y][x].animal == Animal.EMPTY:
                        # 石あり・解放済み
                        judge_board[y][x] = 0
                    else:
                        # 石あり・未開放
                        judge_board[y][x] = 3
                else:
                    # 石なし
                    judge_board[y][x] = -1
        # 配列返却
        return judge_board


# マス目管理クラス
class Cell(object):
    def __init__(self, animal, stone):
        """ 初期化関数
        """
        self._animal = animal
        self._stone = stone

    @property
    def animal(self):
        return self._animal
    
    @property
    def stone(self):
        return self._stone

    def is_stone_empty(self):
        """ 石が置いていないか確認する
        """
        return self._stone == Stone.EMPTY
    
    def put_stone(self, stone):
        """ 石を置く
        """
        self._stone = stone
    
    def is_animal_empty(self):
        """ 動物がいないかどうかをチェックする
        """
        return self._animal == Animal.EMPTY

    def remove_animal(self):
        """ 動物を取り除く
        """
        self._animal = Animal.EMPTY

def main():
    # ママラスの創造
    mammalath = Mammalath()

    # ママラスの循環
    while not mammalath.is_game_end:
        mammalath.turn()

if __name__ == "__main__":
    main()