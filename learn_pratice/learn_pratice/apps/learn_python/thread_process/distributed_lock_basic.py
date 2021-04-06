


'''

分布式锁是控制分布式系统之间同步访问共享资源的一种方式

    小莱去网吧打游戏，路上碰巧遇到了同学小王和小丁，三人同时来到网吧前台表示都想在包厢里上网。
    但是包厢只有一个，同一时间也只能容纳一人，前台MM很为难。突然，前台MM心生一计，将一枚硬币抛于空中，
    让他们三人同时争抢，谁能抢到谁去包厢。只见小莱眼疾手快最终将硬币据为己有，看着不甘的小王和小丁，哼着小曲进了包厢


分布式锁的场景
    当多个机器（多个进程）对同一数据进行修改时，并且要求这个修改是原子性的，
    (如果把一个事务可看作是一个程序,它要么完整的被执行,要么完全不执行。这种特性就叫原子性)
    那么就要用到分布式锁。例如：秒杀时解决库存超卖问题。


分布式锁的特点
    1、互斥性
        任意时刻，只有一个客户端能够持有锁。
    2、不会发送死锁
        即使有一个客户端在持有锁的期间崩溃而没有主动解锁，也能保证后续其他客户端能加锁。
    3、容错性
        只要大部分的redis节点正常运行，客户端就可以加锁和解锁。
    4、解锁
        加锁和解锁必须为同一个客户端，客户端不能解锁他人的锁

分布式锁的实现
    基于redis实现(基于缓存来)
    基于mysql乐观锁实现(数据库)-->乐观锁/排他锁/数据库隔离
    基于zookeeper实现(分布式系统管理服务)

'''

'''https://blog.51cto.com/15015169/2615577'''
'''https://blog.csdn.net/biheyu828/article/details/89005866'''
'''https://blog.csdn.net/xiazep521/article/details/80594991'''


'''
锁的实现方式，按照应用的实现架构，可能会有以下几种类型：

如果处理程序是单进程多线程的，在 python下，就可以使用 threading 模块的 Lock 对象来限制对共享变量的同步访问，实现线程安全。

单机多进程的情况，在 python 下，可以使用 multiprocessing 的 Lock 对象来处理。

多机多进程部署的情况，就得依赖一个第三方组件（存储锁对象）来实现一个分布式的同步锁了。
'''


'''

2.1，基于数据库的锁：

基于数据库的锁实现也有两种方式，一是基于数据库表，另一种是基于数据库排他锁。

基于数据库表的增删：

基于数据库表增删是最简单的方式，首先创建一张锁的表主要包含下列字段：方法名，时间戳等字段。

具体使用的方法，当需要锁住某个方法时，往该表中插入一条相关的记录。这边需要注意，方法名是有唯一性约束的，如果有多个请求同时提交到数据库的话，数据库会保证只有一个操作可以成功，那么我们就可以认为操作成功的那个线程获得了该方法的锁，可以执行方法体内容。执行完毕，需要delete该记录。

对于上述方案可以进行优化，如应用主从数据库，数据之间双向同步。一旦挂掉快速切换到备库上；做一个定时任务，每隔一定时间把数据库中的超时数据清理一遍；使用while循环，直到insert成功再返回成功，虽然并不推荐这样做；还可以记录当前获得锁的机器的主机信息和线程信息，那么下次再获取锁的时候先查询数据库，如果当前机器的主机信息和线程信息在数据库可以查到的话，直接把锁分配给他就可以了，实现可重入锁。

数据库的排他锁：

基于MySql的InnoDB引擎，可以使用以下方法来实现加锁操作。

在查询语句后面增加for update，数据库会在查询过程中给数据库表增加排他锁。当某条记录被加上排他锁之后，其他线程无法再在该行记录上增加排他锁。其他没有获取到锁的就会阻塞在上述select语句上，可能的结果有2种，在超时之前获取到了锁，在超时之前仍未获取到锁。

获得排它锁的线程即可获得分布式锁，当获取到锁之后，可以执行方法的业务逻辑，执行完方法之后，释放锁connection.commit()。

存在的问题主要是性能不高和sql超时的异常。

'''
'''排他锁（悲观锁）'''
'''

CREATE TABLE `methodLock` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `method_name` varchar(64) NOT NULL DEFAULT '' COMMENT '锁定的方法名',
  `desc` varchar(1024) NOT NULL DEFAULT '备注信息',
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '保存数据时间，自动生成',
  PRIMARY KEY (`id`),
  UNIQUE KEY `uidx_method_name` (`method_name `) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='锁定中的方法';


public boolean lock(){
    connection.setAutoCommit(false)
    while(true){
        try{
            result = select * from methodLock where method_name=xxx for update;
            if(result==null){
                return true;
            }
        }catch(Exception e){
 
        }
        sleep(1000);
    }
    return false;
}
'''