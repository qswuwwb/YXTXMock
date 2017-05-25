#!/usr/bin/python
#coding:utf-8

import re

def name(str):
    result = re.findall('：(.*)\n', str)
    result = [re.split(r',|，', names) for names in result]
    result = sum(result, [])
    result = [name.replace(" ", "") for name in result]
    result = list(filter(None, result))
    return result
str = '''
a.狼类： 饿狼，风尘孤狼，雾风寒狼, 被追杀的狼, 流浪的狼，喜大狼, 暗水天狼，南国野狼, 天峰十三狼，的狼, 小狼, 北方网狼，山中狼，北方寒冬的狼, 苍狼，独狼，伤心狼 , 豺狼, 江湖一狼, 善良的大灰狼，大漠雪狼, 李小狼,

b.鱼类： 小鱼，豆豆鱼，水中的鱼，鱼尾巴，蓝色双鱼, 想飞的鱼，爱飞的鱼，嘟嘟鱼, 溺水的鱼, 淹死的鱼oO, 流浪的鱼，爱哭的鱼, 睡在树上的鱼，海河里的鱼，岸上鱼, 冷冰鱼, 章小鱼, 酷鱼, 半死鱼，嘉楠鱼，蝈蝈鱼，黑鱼崽，深海的鱼, 站在岸上的鱼, 飞奔的鱼, 丢了翅膀的鱼，其名为鲲。逆鳞，与世隔绝的鱼, 夜行神鱼, 飞鱼，翻车鱼, 鱼啊鱼, 小鲜鱼, 白鲨 , 鲸鱼 , 水瓶鲸鱼, 海怪，海星,

c.猪类： 乌溜溜的黑眼猪, 吃饱了晒太阳的猪，脑震荡的猪, 卷毛猪, 虫虫猪，小肥猪, 江湖一孤猪, 飞小猪, 小猪, 会爬树的猪,

d.猫类： 龙猫, 窗台上的猫, 机器猫, 斑点猫, 叼烟斗的猫, 睡猫, 极品肥猫, 狸猫, 老猫，大猫咪，游离状态的猫 ,小黑猫, 天堂里的猫, 逍遥猫, 可子猫, 傻猫, 悠闲的猫, 三猫，

e.狐类： 白狸, 小狐狸, 小美狐，狐媚, 宝贝狐, 冰城飞狐, 狐狸精, 狐狸, 千面狐, 雨狐,

f.羊类： 文羊，山羊, 羊羊，牧羊456，披着狼皮的羊, 牵狼逛街的羊, 肥羊羔, 愤怒的绵羊，筠羊，

g。大型动物类： 疯狂天虎，出林猛虎，北方的虎，虎！虎！虎！，文虎，酷虎, 小虎哦哦，棕熊，啤啤熊，踏雪寻熊, 园园熊, 天上的睡熊, 维尼熊, 霸王龙, 剑神暴龙 , 瞌睡龙，多多龙，记忆中的恐龙, 风云龙, 化骨龙，银龙，小恐龙, 泡泡龙，神龙 , 尊龙，情兽,

h。昆虫类： 小虫虫，老蛀虫, 飞虫, 千年虫, 东东虫, 音乐虫子, 鱼虫子，刚强之虫, 飞虫 , 萤火虫，天蝎の蝴蝶，梦蝴蝶, 玉蝴蝶, 冥蝶, 老茧, 蚕宝宝, 螳螂，蝌蚪，香雪螺, !海螺!，竹蜻蜓, 蜻蜓飞飞, 树影蜗牛，小蜗牛 ,狂奔蜗牛，豌豆蛛, 蜘蛛，网上蜘蛛, 时空蚂蚁, 寂寞的蚊子，草原上的蚂蚱，神秘天蝎 , 牛虻，三只草蜢赛蟑螂,

i。飞鸟类： 风之别鹤, 闲云野鹤, 梢雁，黄河之雁, 雁子，寒潭孤雁, 荆棘鸟, 菜鸟，棘鸟, 林中鸟, 雪候鸟nn， 康.雪候鸟, 恋恋青鸟，蓝色飞鸟, 红头鸟，月月鸟，落单的候鸟, 孤独的鹰, 反恐金鹰, 天津上空的鹰, 天鹰, 海鹰，金翅雕 , 鸿鹄, 恰似惊鸿，沙洲孤鸿, 长天孤鹜, 小枭, 效鹏, 飞鸽, 沙鸥，姬冰燕，白鸦，寒鸦数点, 火凤凰, 雨中飞鹭,

j。其他动物类： 瘦死的骆驼, 大傻兔， 雪兔, 兔哥，流口水的兔子，披着狼皮的兔子, 精灵鼠小妹，汤耗子, 戴小鼠, 小老鼠, 冰松鼠, 耀华河马, 小鳄鱼, 良驹
A.各种草类： 解忧草, 紫色草，孤独的薰衣草，狗尾巴草vs丁香，小草, 叶草, 失恋的小草儿, 凌草, 车前草, 永绿草皮，彼岸草，蓝草, 星星草，兰花草， 彩叶草, 天涯湘草, 海草,

B。各种树类： 老榕树,梧桐，雨桐, 柳，早春新柳, 独叶树, 望树, 水木, 蓝槐，古松树, 蓝杉, 杉林, 白枫, 聂枫, 白杨, 百步穿杨, 森林, 林子, 丛林赤枫, 叶自飘林, 雾岛之樱,

C。花卉类： 处女座的玫瑰花，?玫瑰, 落泪玫瑰, 带刺的玫瑰，开心玫瑰，没有绿叶的红花, 郁金香, 雨在下的菊子, 童梅, 狮子座向日葵, 罂粟花, 江南采莲, 夏侯兰，网路昙花, 彼岸蔷薇, 永远的蔷薇，卉儿卉儿, 小花，洛神花，紫丁香, 死亡樱花, 伤花怒放,

D。其他植物类： 蒲公英, 荷叶小露, 菜菜子-521 ，采帅哥的小蘑菇, 芦苇，一片小叶子，秋天的叶子, 随风落叶，飞叶, 柠檬树叶，香焦叶，叶仙儿，枫叶112 ，木棉，今日斑竹, 公孙束竹, 风信子, 清水幽萍, 豆豆蔓, 白木瓜，甘蓝子，夜蔓, 马喜藻, 槲寄生,

3.数字类： (因人数众多及名字无从实意考察，故大部剩去。。以典型常客概之，下同：）

123456999，46604657, 33010136, dhui_19, 002010208, 002010103, yoyo520 , snys9494 ，wb0002052 ，andy735757， wang51613429, pp8848 ，454566，h_j30000， hjyy8819821009, qiqi000000, ezhe10000，fxn214，fjx1982441，less3366， fangjin5217758，rain668899, m800618127, lyd84604，cf751125， water221638，s8760，aa2020，27409654，upup2010, sammy00210909, ，jwj_789456，l15335803， zhao831110，zj_13938, wenlu_010010, z19850629, fly800725, 一凝, 零零幺, 爆一点，1，么，2，啊二, 阿三，三子, 左四, 老五, 啊六, 阿七，七七,

4。天文气象类：

A.风类： 秋风，远风，栩栩清风，竹影清风，夜风, 寒风, 天堂的风, 南来风，风继续吹, 风之引力，海上追风，蓝风，萧风, 张狂的风, 风在云颠，流浪的疾风, 清风, 天风, 沉默风，东野牧风，黑狐无风，牧野静风，淳风, 舜风, 朔风, 自在的风, 往日随风, 自由如风，爱晒太阳的风, 淡淡的风, 笑凌风,

B。云类： 石映飞云, 悠悠云，紫竹星云，天业云, 风云突变，风云再起, 云曦, 悠悠云, 水云, 流云,煦风行云, 沧海行云, 风云2002 , 步惊云,

C。雨类： 十一月雨，零星小雨，雨在下，雷雨, 期雨, 细雨霏霏, 雾雨，凝固的雨，雨一直下, 清雨, 水晶花之雨, 小小雨，流星雨_74，紫雨，冬雨, 毛毛雨

D。冰雪霜雾类： 纳兰飘雪，飘雪的季节, 暮成雪，夏雪, 凝雪，季节的雪, 天之雪，暴雪, 萧雪 ,太白有雪, 北雪, 前田莞雪，白雪飘飘, 奇冤待雪, 冰洁雪儿，飞花坠雪，南极雪, 雪清爽，雪千寻, 冰凌雪儿, 雪花飞扬，百里冰, 冰凝 ，燃烧的冰，薄荷冰，红豆冰，寒&霜, 水莲雾, 玉喋霜儿, 雾水, 凌云露，炽热的冰雪, 坚冰, 任性紫冰,

E。日月星辰类： 101℃太阳，晨曦骄阳，落日, 醉阳，余夕阳，红月亮，秋天的月亮，水中月，水间苍月, 北方苍凉月，星星 ,大侠蓝星，蓝星，流星，夜之流星, 冰雨星，龙星, 繁星, 凡星, 满天星*^_^* , 漂浮的星儿, 新月晨星 , 大漠孤星 , 木卫三, 仰望星空, 今夜星光灿烂, 星河, 雪舞银河,

F。其他气候类： 天空依然阴暗，天气真好，月日天，日芯, 蔚蓝天空，橙色天空，朋友的天空，天马行空，易帧天，小乐天，东方晓晨，迷夜，夏之夜，清夜，不夜之侯, 迷夜，浪涛, 浪花, ?浪很小, 力挽狂澜，飞舞月光，阳光，PK光, 原色阳光-3, 都市阳光，沙尘暴, 脆弱的空气，琴心剑气, 陌上纤虹，彩虹, 虹儿, 雨后惊虹，尘土飞扬, 冷锋, 无烟, 雷雷, 闪电光芒, 房凌，海市蜃楼, 辐射，风旋,

5。美好女子类：

萍萍，雅婷，雅雅, 雅楠, 雅雯, 稚雅, 苏珊，海琳 , 安琪儿，晓瑷, 容容，晶莹，清水美人, 黛儿, 紫璇, 美子，梦如, 楚楚, 紫嫣，娴雨婷，梦晶, 静伊，彤彤,小菲, 馨儿微安, 简单萱萱, 诗婕, 云馨, 相奈儿, 絮儿, 颦儿，蓝齐儿, 碧珊, 雨婷雨婷, 茜茜, 明慧, 东美，雪婷，洁娜kina ，kobe菲菲, 雨莹,

6。东西日用品类：

反方向的钟，电灯泡，痰盂, 板凳, 簸箕簸箕, 蓝色手表, 窗帘, 刀片, 口红, 买女孩的小火柴，铁锤，小榔头, 寂寞的cd机，童心小镜子, 水桶，救生圈，弹簧，发动机V8，机器零件, 黑白天平, 罐子, 沙漏, 透明罐子, 蓝色香水瓶, 铃铛, 红铃铛, 风铃, 玻璃耗子，水晶叶子, 石头.剪刀.布, 伤口上的盐, 玩具, 发条兔子, 火花7588, 花心筒，木墩，唱片, 外挂滤镜, 哈哈镜, 哭泣的键盘, 黄书包, 纸菊花, 塑料荷花, 水之印, 蜡烛, 千千结, 烟花, 冰箱^, 猫眼 , 双色猫眼se , 天样纸 , 红丝砚, 吧吧炉,

7。汉语拼音类：(因人数众多及名无从实意考察，故大部剩去。。）

aaaa05120566, baoshiyu1988 ，beijingqiu, benbenlong002, changchang, guxinjian1026，guojun， fengjikou, juanzi, jiangwanying, huoyezi, kaifeng, liweijie，laopengyou, liushuixinqing，maozi, nangonglei, qicaihong, Suzanna, shuixiang, tuoxie, wenfei001 ，wawa, weiziji，xiaoxiancai，xinxi, xianggelila, yangkeli, zhangyang，hahacoon，zhanghongt
A.江河湖海类: 水啊水, 伊水，秋水，春江水, 上善若水，水澜, 流水, 行云流水, 绿水悠悠，幽幽蓝水, 似水，流动的水, 凌乱如水 加勒比海蓝，振海，舒适海, 文海，云海, 风影海，广海, 望海, 天堂海, 平镜海岸，伤心太平洋, 百里溪, 兰溪，溪乐，湘江2001, 我爱黄河, 南河，

B.其他类： 香山, 乔山, 大雪山, 金山, 江山，爱苍山, 枫林火山，丘岳, 唐晨峰, 宝剑峰，梦想之巅, 梦海之巅, 江城子, 极地，海内比邻，料峭, 峭壁, 流泪谷, 死亡谷，鬼谷幽道 , 原野, 晓野, 杨柳岸，池塘边, 兰汀, 孤岛, 怪岛, 双桥, 多情沙滩, 迷路的地图 , 天涯海角，沙漠超，滨江大道东，一品泉，源泉, 潭深深，凡高的麦田, www.菜地.com, 鼓浪屿, 蒋南亚, 北国风光，云和山的彼端, 雨界, 懿州, 神州行, 纳木错，橙色荷兰，漠河，承德露露，英格兰，黎巴嫩，麦嘉, cccp，

9。身体五官类：

大牙，没有蛀牙， 半张嘴, 跷跷鼻, 怀恋头发, 长发飘飘，头发总也长不长, 三毛, 黄毛, じ爱眉, 蓝眉，汪艺眉, 灰色的眼睛，第三只眼, 风之眼，斗眼，四眼, 九眼，木眼, 蓝颜, 海瞳, 心儿, 无心, 冰冷的唇, 纯唇, 红酥手, 富贵神仙手, 细腰，记者小脚丫, 坚实的臂膀，波波，当左手爱上右手, 中指朝哪, 长了毛的心肝, 醉卧美人膝, 肥肠,

10。有名有姓类：

A.中国类： 张大红, 张无忌 , 奕柯，李拜四, 欧阳费劲, 东方消沉, 张大民 ，张二民, 高天乐，朱维妙, 范哲, 范峻, 孙益申, 宋晓培，苏菲, 梁婉婷, 吴逸, 吴雨, 陈良昱, 凌无卿, 魏风华, 马可可, 周鼎, 周子安, 坤哥9597, 任莹莹, 刘占宇，崔元晖，王小柔, 凌昕，梁婉婷，杨建雄, 小文，小冉，子安，陈西，老杰, 老明 ,杨胖胖, 李文, 李剑，李霖, 许锰, 刘克谦, 东方聊天，爱新觉罗静静 , 令狐帅帅, 上官小仙,

B。外国类： 农民卡尔，人品太次郎, 健次郎, 大门五郎，小泽健次, 南海十三郎, 伊藤英明, 则卷千兵卫,

C。名人类： 唐僧gg，八戒, 猪小戒， 悟空, 车寅次郎, 公子襄, 晏子, 苏武，勾践 , 轩辕黄帝, 炎帝, 炫烨, 虹一法师，本拉登, 缪斯, 查拉图斯特拉, 苏格拉底, 亨利八世, 莎士比亚, 拿破伦二世 ,道拉格斯, 奥力芙, 致命朱丽叶, 卡内基, 摩西，乔丹，巴乔, 巴蒂1988， 王治郅， 李珊，施连志, 张效瑞，老亮, 帅根伟，卡西莫多，骑天大圣, 西门庆, 林妹妹lucklili, 华安, 喜儿，周润发，金庸，好兵帅克，

11。军队武器类：

匕首与投枪，古震剑，莫名剑, 刻舟求剑, 魂刃斩, 倚天剑, 依天舞戟, 双截棍, 石弓, 西风断刀, 义枫刀,
12。医药类：

免疫针，消渴止咳贴，后悔有药，维他命, 毒药，绯雨闲丸， 维生素, 伟哥, 大壮, 陈皮, 流行性感冒，健康之友, 大补，肾掉打下，运动医学，

13。缩写代号类：(因人数众多及名无从实意考察，故大部剩去。。）

aocool, aiw-520, aljj, btz1982, basc520, bx99，b8858，cctv2，cwfcwf, d.s., ggd_520,efg222，fzdgs, fmz_84，fox_yz3_411, ggnnzz,GP-02 ,hjh_h, jsntcj, khw_79, lili88_sisi, le625cn, jllsr，mail1974, n10, ncjncj，pp8848, solk_yt, TACO, TACO, ufo,we45, wqh，xxys，xdcyxj, xysgod, yydd0, z_l_j，yoyo520, JACKYMC, z-w-b，snys9494, zzmmhtd,zxcvzxcv,wwwxcomcn,vivivivi,ph7，txwd， Hdwei，TMBD， w11w1y，a7man1314，y5kcn，nnoo，gooooogle，ALEXSZB，tftlj，Me￡，hsbzcb，zzzzzz,

14。芸芸众生类：

A。侠客类： 影子杀手，老杀手, 女特工，零零漆, 白金圣斗士, 蒙面行者，武士，剑士，追风侠, 饮风游侠，,ok小飞侠, 少侠一号 , 神雕大侠, 有爱游侠, 侠客，胖子侠客， 沙客，逐浪客，三剑客, 海陵客，健啖客，雨夜故客，世纪过客，闲散过客，新房客, 天涯孤客, 闪客, 听风客, 大内密探, 保镖,

B。皇戚类： 公主，香香公主, 青蛙公主，皮蛋公主，槟榔王子, 幽境王子，吹萧公子，情歌王子, 忧郁王子，冰王子，论语之王子, 孤独王子-青蛙，太子, 格格HOCKEY, 倪二公子，

C。男女性别类： 小男生，BAR斯文男生，另类女生，透明女生，kt斯文女生，银河女生, 薄荷女生，占美妹妹, 球妹，菲妹, ppmm_冰女儿，山里妹，猪猪妹, 丫头子, 加非妃，玉女 , 文清姐姐，瓶子里的女人, 靓女人8888，西子姑娘, 拇指姑娘, 超及无敌美少女, 女情人，红颜知己，她她, 美女2，白兔先生，倒影先生, 风云男子, 粉色男人，一般男人, 辣哥，阿一哥, 北方的郎, 南海十三郎, 津城帅哥, 放浪兄弟 , 楚国小生, 野小子，追梦小子，好穷小子，流星小子，邢国小子，飞腾小子, 猫少爷, 大少, 咱爸咱妈, 菌男 ，宜男,

D。天使类仙子： 天使, 找乐天使，马路天使, 飚风天使, 极度天使, 邪天使 ,永远的复仇天使，妖翼天使，折翼天使，堕落天使，碧波仙子, 芙蓉仙子, 紫霞仙子，天仙子，飞天090,

E。坏蛋类： 黯然骗子, 骗子, 大海盗, 北欧海盗Viking，蝇木花盗，采花贼，我是流氓 ，帮主 ，黑帮, 恐怖精英, 古惑仔, 极度痞子, 一代球痞，文学痞子, 好摄之徒, 消息贩子，匪兵甲, 人贩子姐姐, 明天坏女人, 江南地主，板砖手甲
小人物类： 过路人, 群众甲, 游客甲, 观众丁, 小伙计, 打工仔, 一品石匠, 臭皮匠, 翠花, 觉醒的奴隶，飞奴, 小牧童，小哨兵，小干探, 小丑，

G。智障病残类： 傻蛋，高智商傻子 ,白国际, 小笨，笨丫头，笨鸟先生，傻， ysyg聪明了, 糊糊, 智障人士，老愚，装淑女，哑女，哑巴, 上海神经, 林有病, 风语者 , 确实色盲, 狂人癫语, 不醒人士，中国患者, 弱智学校校长,

H。各种人类： 街头诗人，流浪文人, 风雨哲人, 化乙散人, 水西散人, 伊人, 燕北闲人，第一号伤心人, 第12人，第三种人, 天津人, 正义的天津人，静海人，中国人, 武清人, 山顶洞人, 神秘人, 好心人，马善人, 伞中人，铁面人, 外星人, 雪人, 孤独人，主持人，出国人, 都市猎人，钢铁猎人, 多情猎人, 庭前人, 趋势主人, 天堂主人，眼镜超人，橡皮模拟人, 玫瑰情人, 都市稻草人, 寻树人, 边缘人, 寻梦人, 何人, 旧日的某人, 神秘人X, 动感超人, 清爽伊人,

I。子者迷类： 漫步者2017, 漫游者，麦田守望者, 迷球者, 红颜与行者, 失落者, 先锋者, 伪装者, 好问者, 使者，忍者1，亡之影者, 三清幽者, 万人迷, 假球迷，真心球迷，钢杆球迷，球迷pp, 官儿迷, 黯然浪子，宽带之子, 欢子, 北大浪子, 三德子, 狂世才子, 今语子，老夫子,

J。其他三教九流类： 将军, 救世主，灌水高手, 天津操盘手, 高高手，益康大夫, 居律师, 大副，水手，站长, 中国足球运动员, 队医, 全国第三 , 日人民报评论员，丘比特的小跟班, 逍遥随从，小熊在江湖，海上人家, 渔夫, 等兔子的农夫, 津门百姓， 豆花庄庄主，二当家的，三掌柜的，觉主，顽主, 导游, 北京大爷, 老汉, 门老伯, 云之君, 荣誉勋章奇袭先锋, 小学语文老师, 中学生, 毕业生, 齐天情圣, 新?的，整蛊专家，佑派, 活宝, 三爷的后辈, 文盲,

15。颜色类：

祖母绿, 大红 , 银灰色，妍色，灰色，深灰色，黑与白, 金色，蓝色的, 未蓝，暴暴蓝, 天天天蓝, 海蓝色，淡蓝蓝蓝, 忧郁的蓝色, 暗夜深蓝, 澄，紫青, 蓝2000, 郁蓝, 瓦蓝, 浅蓝色, 珐蓝，雨逸蓝, 黑痕, 黑幻, 东方白, 冷色系, 风的颜色, 无色彩, 十二种颜色，百媚千红,

16。各种心类：

清心, 隐心，好心, 京心, 水心，将心比心, 漂流的心, 柳之心, 紫色芳心, 冰冻的心, 任我随心, 可心，良心，霜心 , 是非心, 月斜天心, 弦月眉心, 绯村剑心, 来自我心, 心非，酌幽心, 潮湿的心，

17。诗情画意类：

水云之间，烟久如画，清风月影, 残荷听雨, 浮云过影, 竹影清风, 寒光竹影, 水清云淡, 云雨飘零，红叶漂浮947，叶随雨落，吟雪情枫，青色雨音, 踏
雪无痕，踏雪寻梅, 蝶梦无边，蝶舞风飞，小桥流水人家, 听到涛声， 逝水无痕，清水幽萍, 雨夜追风, 绿水悠悠, 风生水起，漾漾涟漪, 无声胜有声， 静夜漫思, 晚秋骄阳, 风烛人家, 望月追忆, 春眠不??, 极目楚天, 烟锁寒楼，散钓风光, 冷月无声, 邂逅黄昏, 枫林叶落, 天镜云生，泽风飘渺，月夜星辉，山秀溪清, 月影沙丘, 风在云颠, 梦海之巅, 空山幽兰, 一叶知秋, 雁过留香, 水清云淡,

18。不伦不类类：

极度赫赫，爬来爬去，倒霉催的, 个个，北方叉叉, 不知火，虫二, baby不卑鄙, 巴巴变~！，果布奇然，笑?，吐~~ ，蚊子也放屁，可以吗，FM18CEO，中国猪的协, 比烟花还寂寞, 为你跳海, 霸波奔, 千与千寻, 唐伯虎点蚊香, 五里雾虑喋, star_闪亮登场，陪熊去看硫酸雨, fbi_让你难琢磨，生物酶是什么丫, 挑战腐败教师, 五里雾虑喋 , 哈韩爱俊，蔡慧玉滋，臭名昭著相见欢, 北方衰衰, 血手杜杀, 五影五行, 玫菲涩妩, 祁小贝R燕鸣，菌临天下, 乜獬豸, 莫名其, 悲酥.清风.电, bb啊,

19。食品类：

A。瓜果糖类： 绝代“水果”，水中的苹果，青苹果cici, 哈哈苹果，可爱的草枚, 李子栗子梨, 花梨, 香蕉魅力，葡萄, 橘子，红橘子, 红橙子，香橙, 柳橙，阴天的桔子, 柿子, 北方蜜糖, 吹泡糖, 完美泡泡糖, 牛奶糖糖，棉花糖, 奔跑的巧克力, 柠檬，荸荠,

B。零食类： ぺ灬ｃｃ果?ル，罐头，冰淇淋, 开心米果, 夏天的果冻, 曲奇多, 紫布丁,

C。饮料类： 咖啡泡泡，冰咖啡，苦咖啡, 煮不开的咖啡, 黑色咖啡, 低调咖啡 ，咖啡效应 , 咖啡的幻想 , 咖啡不加糖, 咖啡加冰水, 雀巢302, 咖啡伴侣, 红茶，冰茶，泡沫红茶，蓝色多味茶, 茉莉茶，淡淡清茶, 冬日柠檬茶，雪碧-13, 稀释的果汁 ，紫红色蓝莓酸奶，草莓酸奶, 可乐加冰, 可口可乐, 老醋,

D。粮食菜蛋类： 萝卜，大个萝卜, 男瓜，大冬瓜 , 小号茄子, 菜花儿, 空心菜，红@豆, 秀豆豆, 玉米0117，小米，粟米, 天津麦子, 舞蹈的麦，赤耳红穗, 青豆, 豌豆，小姜，一车鸡蛋, 茶叶蛋，茶鸡蛋，蛋蛋, 热爱红旗的蛋 , 毒蘑菇, 采女孩的大蘑菇,

E。饭菜席类： 四喜丸子，烤全猪, 烧烤, 椒盐麻雀, 蘑菇小丸子, 拔丝荔枝, 酸菜炒米，皮蛋106c, 粉色雪丽糍, 绝望的生鱼片, 天津饭，大米饭, 鸡子面，果子, 杂酱面, 天之饺子，清汤挂面，绿豆粥, 汤圆, 花样年糕, 火锅加冰, 麻辣烫, 泡面可乐, 网络小菜, 虾皮,

20。理论法规类：

28法则，现实主义，游戏主义，鹰派宣传组1, 小革命, 恋爱革命，机会主义，痛苦的信仰，

21。爱情类：

远离爱情，情剩，ZT缘
，萍水相逢，爱萍水相逢, 枯缘，也许我爱你，?的就是? ，等你爱我 ，爱不爱, 捡爱, 爱, 爱死你， 有多少爱可以胡来, 没有你的爱, 很爱很爱你，情义无价， 风尘之恋，我爱“烟花”, 我爱?argentina, 爱情如流星划过， 爱真的需要勇气， 因为爱所以爱， 爱你一万年11111，错爱一生，爱没有理由, 爱如捕风， 缘来有你，相思风雨中， 我只在乎你, 感觉你的存在, 有你真幸福, 当我遇上你，想雨也想他, 新不了情, TJ酷盖不帅别爱, 等你回来， 戒情人2002，爱警, 一切都是为你, 爱津永恒, 那么爱你为什么 , ?欠?已停?，那一见的风情, 爱我没错, 一个人爱, 无妻徒刑, 不谈感情,

22。歌舞器乐类：

风笛, 键啸, 苍海笛声, 婆罗门之歌，恋爱休止符，浪漫的音符, 水蓝色的旋律，特离谱 ,可乐音乐，雪碧音乐, 靡靡之音, 轻歌曼舞，凤舞, 凤舞翩翩, 群魔乱舞，樱雨忧舞，街舞, 星舞, 与狼共舞, 龙腾凤又舞, 舞雨火, 不如跳舞, 晓歌, 煮酒嚎歌, 纷乱的节奏，节奏自由，缘月无音, 织音, 默音, 琴感，仙乐one飘飘, 老树皮乐队，吉它弦, e弦知音, 香港十大金曲, 摇滚乐狂,

23。崇洋媚外类：(因人数众多及名无从实意考察，故大部剩去。。）

arms, aocool, bluedsky ，bluebell周, blueteethxx， casio，colour, CoolApple，ellen, edoctor0804, feeling-yao ，fishbonegirl, flyingfish, quite718， kaiserin, keenboy，inic，I'm rain, irelandcoffee, lovey, linux_open_lab, luckygirl，lucklili, love_bb2002，forver， libary，lookme1234, lee_larry, maverick, noname，okboy，keenboy, raymond, Dreamover， spirit.wan , しovの俊熙 ，means ，manager852，means，foxworld， redorange, slayer ，sunboy，sungirl330, swallow，spirit.wan , try_again，vaur_han，wolfman228, yamasaki, yesyes1， zxsesame,zstone, 丹尼尔20 ，烈斯达，三星怡灏, 门迭塔, 卡布奇诺, 卡德蕾拉 ，威廉, 亚瑟, 卡米啦，美国甜心, 凯拉斯, 菲布里左，海格里斯, 艾德里亚, 修一郎, 迷洋, 小洋，范特西 , 东皇太一，怀斯曼， 梅格瑞恩, 加尔福特, 阿里努亚, 樱木花道，史特, 藤瑭静伊, 西星希子，克劳馥, 伊诺尔,

作者：法则_28 日期：2003-3-1 13:15:45

接上近3000人网名大全备忘录！（2）

24。建筑设施类：

A。建筑类： 蓝水园, 菁菁校园，失乐园, 流行花园, 流星花园，心灵家园， 结艺坊, 最后一盏路灯，静夜街边灯, 心情电梯^^ ，台阶, 流星街, 穷街, 谱路，八神庵, 文道寺, 风满楼，再过秦楼, 楼上楼下, 斜阳西楼 , 紫轩, 潇洒出阁, 妙语轩, 清梦小轩, 梦之轩, 伊轩, 月亭亭, 寒小门, 谁在敲门, 中流砥柱, 心情车站，再别康桥, 西城，山间的小茅屋, 村上，深深房, 雍风妙舍,
寂寞酒吧, 青天井，晓井, 防空洞，燃烧天堂，地狱天堂, 火柴之天堂，001100库, 家庭旅社, 大?, 资源规划署，

B。建筑材料类： 三合板, 墙上的另一块砖, 沙子, 粒砂， 风雨蓝砂, 意中沙315，恒河沙, 石头, 山上石, 月亮蓝石头，蓝石头, 墩子, 顽石, 夏石，石石石, 真石, 某种物质,

25。神鬼类：

幽灵日记，神秘天蝎 ，慢慢的我成了吸血鬼 ，我是妖怪, 冷星魂, 冷月葬花魂, 午夜游魂, 大眼勾魂, 活神的姘，死神的妾，人间妖孽, 灵魂腐蚀, 忐忑幽灵, 金色的骷髅, 变相怪杰, 魔鬼爱人，小妖女 ,小女巫, 小魔女, 小东邪, 活着的死人，山村小尸, 老尸， 第二个灵魂，天使爱上吸血鬼, 中场灵魂，暗黑精灵，睡之精灵, 希腊神话，神话, 许灵, 吸血伯爵, 精灵巫婆, 飘灵儿, 骨之精灵, 凌冷妖, 海妖, 青铜狂魔, 海妖, 金色夜叉, 兰色精灵，小丫精灵, 九鬼嘉隆，与魔鬼共骑, 天堂魔鬼, 桃谷六仙, 受砚潜灵, 水精灵, 神秘之符, 海灵子, 精灵, 空灵, 逍遥神, 诸神, 古月神仙, 雪的守护神, 神仙, 老仙儿, 杂神,

26。无用杂物类：

小愚木头，木头，半根烟，垃圾1999, 汗脚鞋垫, 天津瓶子，空瓶，老树根，白树根, 泥巴, 拖泥, 补丁, 灯芯, 红苹果核，泡泡沫沫，小泡泡，面具一半,

27。灰尘类：

消失?埃，梧桐的灰烬，掸落的灰尘, 飞翔的尘埃，雨尘, 若尘, 凡尘, 一尘, 飙尘, 尘埃，涤尘，恋恋风尘7987, 死灰复燃, 沉香屑,

28。心情类：（网友们如果仔细研究,就可以看出是描写一个女孩失恋后的心情的词汇串联）

'''

names = name(str)