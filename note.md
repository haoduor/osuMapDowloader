##model
实例化的对象

##mapper
把对象持久化
- maps 地图的实例
- beatmaps 小图谱的实例与maps做关联

##service
完成功能
1. 自动爬取所有的图谱
2. 根据本地的图谱免除下载
3. 多线程下载图谱


##task
可以辅助完成service 的小工具

##spider
从网络获取json数据
需保证线程安全

##adapter
格式化json对象成model
