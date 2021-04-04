
import time
import pymysql



'''
        db = pymysql.connect(user='root', database='test')
        self,
        *,
        user=None,  # The first four arguments is based on DB-API 2.0 recommendation.
        password="",
        host=None,
        database=None,
        unix_socket=None,
        port=0,
        charset="",
        sql_mode=None,
        read_default_file=None,
        conv=None,
        use_unicode=True,
        client_flag=0,
        cursorclass=Cursor,
        init_command=None,
        connect_timeout=10,
        read_default_group=None,
        autocommit=False,
        local_infile=False,
        max_allowed_packet=16 * 1024 * 1024,
        defer_connect=False,
        auth_plugin_map=None,
        read_timeout=None,
        write_timeout=None,
        bind_address=None,
        binary_prefix=False,
        program_name=None,
        server_public_key=None,
        ssl=None,
        ssl_ca=None,
        ssl_cert=None,
        ssl_disabled=None,
        ssl_key=None,
        ssl_verify_cert=None,
        ssl_verify_identity=None,
        compress=None,  # not supported
        named_pipe=None,  # not supported
        passwd=None,  # deprecated
        db=None,  # deprecated
'''





# cursor.execute("""
# CREATE TABLE IF NOT EXISTS runoob_tbl(
#    runoob_id INT UNSIGNED AUTO_INCREMENT,
#    runoob_title VARCHAR(100) NOT NULL,
#    runoob_author VARCHAR(40) NOT NULL,
#    submission_date DATE,
#    PRIMARY KEY ( runoob_id)
# )ENGINE=InnoDB DEFAULT CHARSET=utf8;
# """)

def db_test(sql):
    # 打开数据库连接
    db = pymysql.connect(user='root', database='test')
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()
    # print(cursor.fetchone())
    # print(cursor.fetchmany())
    data = cursor.fetchall()
    print('----len----%d----' % len(data))
    for i in data:
        print(i)
    # 关闭数据库连接
    db.close()


sql_list = [
    # 面试 SQL整理 常见的SQL面试题：经典50题
    # https://blog.csdn.net/u010565545/article/details/100785261/
    # '''select * from apps;''',
    # '''select distinct country from websites;''',
    # '''select * from access_log where count > 100;''',
    # '''select * from websites where alexa between 10 and 50;''',
    # '''select * from access_log where count in (100, 20, 102);''',
    # '''select * from apps where url like '%qq%';''',
    # '''select * from websites where name like '_o%';''',
    # '''select count, aid from access_log where count < 200 order by aid asc;''',
    # '''
    #     select *
    #     from websites
    #     where (id > 0)
    #         and (name in ('Google', 'Facebook'))
    #         or (alexa between 1 and 100)
    #     order by alexa asc ;
    # ''',
    # '''select aid, site_id, count from access_log order by aid desc, count ;''',
    # '''insert into apps (app_name, url, country) values ('app2', 'fdsds.com', 'us');''',
    # '''insert into apps (app_name, url, country) values ('app3', 'fdsasd.com', 'us');''',
    # '''select * from apps;''',
    # '''delete from appsbak;''',
    # '''insert into appsbak select * from apps where country = 'us'; ''',
    # '''update appsbak set country = 'CN' where id = 1;''',
    # '''delete from appsbak where id = 1;''',
    # '''select * from appsbak;''',
    # '''select * from apps;''',
    # '''select top 3 * from appsbak;''',
    # '''select top 20 percent * from appsbak;''',
    # '''select * from websites where url regexp '[^oo]';''',
    # ''' insert into appsbak (app_name, url, country) values ('淘宝 APP', 'fdsaxxsd.com', 'us');''',
    # '''
    #     insert into websites (name, url, alexa, country)
    #     values ('stackoverflow', 'http://stackoverflow.com', 0, 'IND');
    # ''',

    # '''
    #     select w.id , w.name, a.aid, a.count, a.date
    #     from websites as w
    #     inner join access_log as a
    #     on w.id = a.site_id;
    # ''',
    # '''
    #     select w.id , w.name, a.aid, a.count, a.date
    #     from websites as w
    #     left join access_log as a
    #     on w.id = a.site_id
    # ''',
    # '''
    #     select w.id, w.name, a.aid, a.count
    #     from websites as w
    #     left join access_log as a
    #     on w.id = a.site_id
    #     where a.site_id is null ;
    # ''',
    # '''
    #     select w.id, w.name, a.aid, a.count
    #     from websites as w
    #     right join access_log as a
    #     on w.id = a.site_id;
    # ''',
    # '''
    #     insert into access_log (site_id, count, date) values (60, 111, '2016-03-19');
    # ''',
    # '''
    #     select w.id, w.name, a.aid, a.count
    #     from websites as w
    #     right join access_log as a
    #     on w.id = a.site_id
    #     where w.id is null ;
    # ''',
    # '''
    #     select w.id, w.name, a.aid, a.count
    #     from websites as w
    #     full outer join access_log as a
    #     on w.id = a.site_id
    # ''',
    # '''
    #     select name, country from websites
    #     where country = 'CN'
    #     # union
    #     union all
    #     select app_name, country from apps
    #     where country = 'CN'
    #     order by country ;
    # ''',
    # '''
    #     select w.name, w.url, a.count, a.date
    #     into websitesBak
    #     from websites as w
    #     left join access_log as a
    #     on w.id = a.site_id
    #     where country = 'CN';
    # ''',
    # '''
    #     insert into apps
    #     (app_name, url, country)
    #     select name, url, country
    #     from websites
    #     where country = 'IND';
    # ''',
    # '''
    #     select * from apps;
    # ''',
    # 只复制表结构
    # '''
    #     create table xx1_apps like apps;
    # ''',
    # '''
    #     create table xx3_apps as select * from apps where 1=2;
    # ''',
    # '''show tables;''',
    # 复制表结构及其数据
    # '''
    #     create table xx4_apps as select * from apps;
    # ''',
    # 在 SQL 中，我们有如下约束：
    #
    # NOT NULL - 指示某列不能存储 NULL 值。
    # UNIQUE - 保证某列的每行必须有唯一的值。
    # PRIMARY KEY - NOT NULL 和 UNIQUE 的结合。确保某列（或两个列多个列的结合）有唯一标识，有助于更容易更快速地找到表中的一个特定的记录。
    # FOREIGN KEY - 保证一个表中的数据匹配另一个表中的值的参照完整性。
    # CHECK - 保证列中的值符合指定的条件。
    # DEFAULT - 规定没有给列赋值时的默认值。
    # '''
    #     create table orders(
    #         o_id int not null,primary key,
    #         o_number int not null,
    #         p_id int foreign key references person(p_id)  -->1 sys_name
    #         constrint pk_name foreign key (p_id) references persons(p_id) -->2 have your pk_name
    #     );
    # ''',
    # '''
    #     # 表已被创建时
    #     alert table orders
    #     add foreign key (p_id)
    #     references person(p_id)
    # ''',
    # '''
    #     alert table orders
    #     drop foreign key xxxname
    # ''',
    # '''
    #     # MySql 中如何删除未命名的外键？
    #     # 删除外键需要知道外键的名称，如果创建时没有设置名称则会自动生成一个，你需要获取改外键的信息。
    #     # 使用以下命令获取外键信息：
    #     SELECT *
    #     FROM
    #       information_schema.KEY_COLUMN_USAGE
    #     WHERE
    #       constraint_schema = <'db_name'> AND table_name = <'table_name'> AND
    #       referenced_table_name IS NOT NULL;
    # ''',
    # '''
    #     create unique index app_index on apps (id);
    # ''',
    # '''
    #     drop index app_index on apps;
    # ''',
    # '''
    #     alter table apps
    #     add column_name xxx;  # or  add column column_name xxx;
    # ''',
    # 1、视图隐藏了底层的表结构，简化了数据访问操作，客户端不再需要知道底层表的结构及其之间的关系。
    # 2、视图提供了一个统一访问数据的接口。（即可以允许用户通过视图访问数据的安全机制，而不授予用户直接访问底层表的权限）
    # 3、从而加强了安全性，使用户只能看到视图所显示的数据。
    # 4、视图还可以被嵌套，一个视图中可以嵌套另一个视图。
    # '''
    #     create view  app_view as  # create view [what can i do] as
    #     select app_name, country
    #     from apps
    #     where id >1;
    # #     视图总是显示最新的数据 每当用户查询视图时 数据库引擎通过使用视图的 SQL 语句重建数据
    # ''',
    # '''
    #     select * from app_view;  # select * from [what can i do]
    # ''',
    # SQL Aggregate 函数
    # SQL Aggregate 函数计算从列中取得的值，返回一个单一的值。

    # 有用的 Aggregate 函数：
    # AVG() - 返回平均值
    # COUNT() - 返回行数
    # FIRST() - 返回第一个记录的值
    # LAST() - 返回最后一个记录的值
    # MAX() - 返回最大值
    # MIN() - 返回最小值
    # SUM() - 返回总和
    # SQL Scalar 函数
    # SQL Scalar 函数基于输入值，返回一个单一的值。

    # 有用的 Scalar 函数：
    # UCASE() - 将某个字段转换为大写
    # LCASE() - 将某个字段转换为小写
    # MID() - 从某个文本字段提取字符，MySql 中使用
    # SubString(字段，1，end) - 从某个文本字段提取字符
    # LEN() - 返回某个文本字段的长度
    # ROUND() - 对某个数值字段进行指定小数位数的四舍五入
    # NOW() - 返回当前的系统日期和时间
    # FORMAT() - 格式化某个字段的显示方式
    # '''
    #     # select avg(count) as avg_count from access_log;
    #     select aid, count   #, count(count) as nums
    #     from access_log
    #     where count > (select avg(count) from access_log)
    #     limit 3;
    # ''',
    # '''
    #     select count(distinct site_id) as num from access_log ;
    # ''',
    # '''
    #     select site_id , sum(count) as nums from access_log group by site_id;
    # ''',
    # '''
    #     select w.name, count(a.aid) as nums
    #     from websites as w
    #     left join access_log as a
    #     on w.id = a.site_id
    #     group by w.name;
    # ''',
    # 在 SQL 中增加 HAVING 子句原因是，WHERE 关键字无法与聚合函数一起使用。
    # HAVING 子句可以让我们筛选分组后的各组数据
    # '''
    #     select w.name, w.url, sum(a.count) as nums
    #     from (access_log as a
    #             inner join websites as w
    #             on a.site_id=w.id )
    #     group by w.name
    #     having sum(a.count) > 200;
    # ''',
    # '''
    #     select w.name, sum(a.count) as nums
    #     from (websites as w inner join access_log as a on w.id = a.site_id)
    #     where w.alexa < 200
    #     group by w.name
    #     having sum(a.count) > 200;
    # ''',
    # '''
    #     # 判断查询子句是否有记录 如果有一条或多条记录存在返回 True 否则返回 False
    #     select w.name, w.url
    #     from websites as w
    #     where exists (
    #         select count from access_log as a where w.id = a.site_id and count > 200
    #     );
    # ''',
    # '''
    #     # MID() 函数用于从文本字段中提取字符 start(起始值是 )  length
    #     select mid(name, 1, 4) as short_title from websites ;
    # ''',
    # '''
    #     select name, url, date_format(now(), '%y-%m-%d') as date from websites;
    # ''',
    # '''
    #     # .用一条SQL 语句 查询出每门课都大于80 分的学生姓名
    #     select site_id from access_log group by site_id having min(count) > 20;
    # ''',
    # '''
    #     # 删除除了自动编号不同, 其他都相同的学生冗余信息
    #     select min(aid) from access_log group by site_id, count, date ;
    # ''',
    # '''
    #     # 一个叫 team 的表，里面只有一个字段name, 一共有4 条纪录，分别是a,b,c,d, 对应四个球对，现在四个球对进行比赛，用一条sql 语句显示所有可能的比赛组合
    #     select * from websites as a, websites as b where a.name < b.name order by a.name, b.name ;
    # ''',
    # 4.请用SQL 语句实现：
    # 从TestDB 数据表中查询出
    # 所有月份的发生额都比 101科目 相应月份的发生额 高 的科目。
    # 请注意：TestDB 中有很多科目，都有1 －12 月份的发生额。
    # AccID ：科目代码，
    # Occmonth ：发生额月份，
    # DebitOccur ：发生额。
    # 数据库名：JcyAudit ，
    # 数据集：Select * from TestDB
    # select accid from jcyaudit where
    #
    # select a.*
    # from TestDB a
    # ,(
    # 	select Occmonth, DebitOccur
    # 		from TestDB
    # 		where AccID='101' group by Occmonth
    # 	) b
    # where a.Occmonth=b.Occmonth and a.DebitOccur>b.DebitOccur
    # '''
    #     select x, (select y from table as b whre b.q = '1' and b.z = a.z) from table as a group by x
    # ''',
    # '''
    #     #   两张关联表，删除主表中已经在副表中没有的信息
    #     delete from table_A where not exists(select * from table_B where a.id = b.id)
    # ''',
    # '''
    #     # 有两个表A 和B ，均有key 和value 两个字段，如果B 的key 在A 中也有，就把B 的value 换为A 中对应的value
    #     update b
    #     set b.value=(select a.value from a where a.key = b.key)
    #     where b.id in (select a.id from a where a.key = b.key);
    # ''',
    # '''
    #     # 1 Java 70    ----> 1 Java 70 pass
    #     # 3 xml  40    ----> 3 xml  40 fail
    #     # https://www.jb51.net/article/80357.htm
    #     select id, name, score, decode(sign(score-60), -1, 'fail', 'pass') as mark
    #     from table;
    # ''',
    # '''
    #     # 含义是跳过2条取出1条数据，limit后面是从第2条开始读，读取1条信息，即读取第3条数据
    #     select * from apps limit 2, 1;
    # ''',
    # '''
    #     # 含义是从第1条（不包括）数据开始取出2条数据，limit后面跟的是2条数据，offset后面是从第1条开始读取，即读取第2,3条
    #     select * from apps limit 2 offset 1;
    # ''',
    # '''
    #     select * from apps limit 2, 5;
    # ''',
]
for sql in sql_list:
    print('-------%s-------' %sql)
    time.sleep(0.3)
    db_test(sql)


'''
            数据集
/*
 Navicat MySQL Data Transfer

 Source Server         : 127.0.0.1
 Source Server Version : 50621
 Source Host           : localhost
 Source Database       : RUNOOB

 Target Server Version : 50621
 File Encoding         : utf-8

 Date: 05/18/2016 11:44:07 AM
*/

SET NAMES utf8;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
--  Table structure for `websites`
-- ----------------------------
DROP TABLE IF EXISTS `websites`;
CREATE TABLE `websites` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` char(20) NOT NULL DEFAULT '' COMMENT '站点名称',
  `url` varchar(255) NOT NULL DEFAULT '',
  `alexa` int(11) NOT NULL DEFAULT '0' COMMENT 'Alexa 排名',
  `country` char(10) NOT NULL DEFAULT '' COMMENT '国家',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Records of `websites`
-- ----------------------------
BEGIN;
INSERT INTO `websites` VALUES ('1', 'Google', 'https://www.google.cm/', '1', 'USA'), ('2', '淘宝', 'https://www.taobao.com/', '13', 'CN'), ('3', '菜鸟教程', 'http://www.runoob.com/', '4689', 'CN'), ('4', '微博', 'http://weibo.com/', '20', 'CN'), ('5', 'Facebook', 'https://www.facebook.com/', '3', 'USA');
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;


-- +----+--------------+---------------------------+-------+---------+
-- | id | name         | url                       | alexa | country |
-- +----+--------------+---------------------------+-------+---------+
-- |  1 | Google       | https://www.google.cm/    |     1 | USA     |
-- |  2 | 淘宝         | https://www.taobao.com/   |    13 | CN      |
-- |  3 | 菜鸟教程     | http://www.runoob.com/    |  4689 | CN      |
-- |  4 | 微博         | http://weibo.com/         |    20 | CN      |
-- |  5 | Facebook     | https://www.facebook.com/ |     3 | USA     |
-- +----+--------------+---------------------------+-------+---------+



/*
 Navicat MySQL Data Transfer

 Source Server         : 127.0.0.1
 Source Server Version : 50621
 Source Host           : localhost
 Source Database       : RUNOOB

 Target Server Version : 50621
 File Encoding         : utf-8

 Date: 05/18/2016 15:52:17 PM
*/

SET NAMES utf8;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
--  Table structure for `apps`
-- ----------------------------
DROP TABLE IF EXISTS `apps`;
CREATE TABLE `apps` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_name` char(20) NOT NULL DEFAULT '' COMMENT '站点名称',
  `url` varchar(255) NOT NULL DEFAULT '',
  `country` char(10) NOT NULL DEFAULT '' COMMENT '国家',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Records of `apps`
-- ----------------------------
BEGIN;
INSERT INTO `apps` VALUES ('1', 'QQ APP', 'http://im.qq.com/', 'CN'), ('2', '微博 APP', 'http://weibo.com/', 'CN'), ('3', '淘宝 APP', 'https://www.taobao.com/', 'CN');
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;


-- +----+------------+-------------------------+---------+
-- | id | app_name   | url                     | country |
-- +----+------------+-------------------------+---------+
-- |  1 | QQ APP     | http://im.qq.com/       | CN      |
-- |  2 | 微博 APP   | http://weibo.com/       | CN      |
-- |  3 | 淘宝 APP   | https://www.taobao.com/ | CN      |
-- +----+------------+-------------------------+---------+


/*
 Navicat MySQL Data Transfer

 Source Server         : 127.0.0.1
 Source Server Version : 50621
 Source Host           : localhost
 Source Database       : RUNOOB

 Target Server Version : 50621
 File Encoding         : utf-8

 Date: 05/18/2016 14:15:39 PM
*/

SET NAMES utf8;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
--  Table structure for `access_log`
-- ----------------------------
DROP TABLE IF EXISTS `access_log`;
CREATE TABLE `access_log` (
  `aid` int(11) NOT NULL AUTO_INCREMENT,
  `site_id` int(11) NOT NULL DEFAULT '0' COMMENT '网站id',
  `count` int(11) NOT NULL DEFAULT '0' COMMENT '访问次数',
  `date` date NOT NULL,
  PRIMARY KEY (`aid`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Records of `access_log`
-- ----------------------------
BEGIN;
INSERT INTO `access_log` VALUES ('1', '1', '45', '2016-05-10'), ('2', '3', '100', '2016-05-13'), ('3', '1', '230', '2016-05-14'), ('4', '2', '10', '2016-05-14'), ('5', '5', '205', '2016-05-14'), ('6', '4', '13', '2016-05-15'), ('7', '3', '220', '2016-05-15'), ('8', '5', '545', '2016-05-16'), ('9', '3', '201', '2016-05-17');
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;


-- +-----+---------+-------+------------+
-- | aid | site_id | count | date       |
-- +-----+---------+-------+------------+
-- |   1 |       1 |    45 | 2016-05-10 |
-- |   2 |       3 |   100 | 2016-05-13 |
-- |   3 |       1 |   230 | 2016-05-14 |
-- |   4 |       2 |    10 | 2016-05-14 |
-- |   5 |       5 |   205 | 2016-05-14 |
-- |   6 |       4 |    13 | 2016-05-15 |
-- |   7 |       3 |   220 | 2016-05-15 |
-- |   8 |       5 |   545 | 2016-05-16 |
-- |   9 |       3 |   201 | 2016-05-17 |
-- +-----+---------+-------+------------+


'''