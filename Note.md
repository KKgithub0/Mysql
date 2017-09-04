1. 更新多表数据
2. 删除多表数据
3. 查询无重复记录
    1. SELECT DISTINCT col_name FROM table_name WHERE condition
4. 排序
    1. DESC降序，ASC升序，默认升序排列，可组合使用
    2. SELECT DISTINCT col_name FROM table_name WHERE condition ORDER BY col1 DESC
5. 聚合
    1. where和having的区别：where在聚合前对数据过滤，having在聚合之后进行条件过滤。
    2. with rollup是否对分类聚合后的数据再汇总
    3. group by聚合
6. 表连接
    1. 内连接和外连接，外连接分为左连接和右连接
7. 记录联合
    1. UNION(去重) 和 UNION ALL
8. ENUM 和 SET类型的区别
    1. ENUM一次只能取一个值，SET一次可以取多个

AUTO_INCREMENT只能用于整数，一个表中至多有一个这样的列，对于此列，应当设置为NOT NULL，并定义为PRIMARY KEY或UNIQUE ，对于InnoDB表，自动增长列必须是索引，如果是组合索引，也必须是组合索引的第一列。

索引：
主键：可以理解为NOT  NULL和UNIQUE的结合，主键其实就是索引，

没有就插入，有的话则更新：
insert into table_name values () on duplicate key update col=value
select有则输出，没有则插入
insert into brand_info(brand) select 'test' from dual where not exists(select * from brand_info t where t.brand='test');
