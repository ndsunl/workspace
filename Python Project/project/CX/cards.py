#-*- coding:utf-8 -*-

class Card:
    """
    功能：纸牌对象，根据属性 suit_id 和 rank_id 创建其他属性 (花色、点数和分值)
    属性：
        suit_id: 花色 1=方块 2=红桃 3=梅花 4=黑桃
        rank_id: 点数 1=A 2=2 3=3 ... 10=10 11=J 12=Q 13=K
    """
    def __init__(self, suit_id, rank_id):
        self.rank_id = rank_id
        self.suit_id = suit_id

        # 创建 rank 和 value 属性
        if self.rank_id == 1:
            self.rank = "Ace"
            self.value = 1
        elif self.rank_id == 11:
            self.rank = "Jack"
            self.value = 10
        elif self.rank_id == 12:
            self.rank = "Queen"
            self.value = 10
        elif self.rank_id == 13:
            self.rank = "King"
            self.value = 10
        elif 2 <= self.rank_id  <= 10:
            self.rank = str(self.rank_id)
            self.value = self.rank_id
        else:
            # 错误检查
            self.rank = "RankError"
            self.value = -1

        # 创建 suit 属性
        if self.suit_id == 1:
            self.suit = "方块"      # 方块 = Diamonds
        elif self.suit_id == 2:
            self.suit = "红桃"      # 红桃 = Hearts
        elif self.suit_id == 3:
            self.suit = "梅花"      # 梅花 = Spades
        elif self.suit_id == 4:
            self.suit = "黑桃"      # 黑桃 = Clubs
        else:
            # 错误检查
            self.suit = "SuitError"

        # 短名，如 4H (红桃4)、JD（方块J）    
        self.short_name = self.suit + self.rank[0] 
        if self.rank == 10:
            self.short_name = self.suit + self.rank

        # 长名，如 4 of Hearts (红桃4)、Jack of Diamonds （方块J）
        # self.long_name = self.suit + " " + self.rank
