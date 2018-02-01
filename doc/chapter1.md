
## 附带源码的编译 ##
```angular2html
./configure
# 编译公共lib库
cd lib
make
# 编译公共lib库
cd libfree
make
# 第一章源码
cd intro
make
```

## 运行程序 ##

### 第一个程序 ###
```
cd intro
./daytimetcpcli 129.6.15.28 # 129.6.15.28为公共时间服务器
```

daytimetcpcli 为从时间服务器获取时间的客户端, 一般时间服务器的默认端口号为13
