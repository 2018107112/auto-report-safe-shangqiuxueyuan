# 商丘学院自动报平安系统
每天2次，采用天翼云自动签到的代码修改而来。 

使用方法  
## 一、Fork此仓库
需要先注册github账号，注册时候需要电子邮件确认。
![](http://tu.yaohuo.me/imgs/2020/06/f059fe73afb4ef5f.png)
## 二、设置工号和手机号
在Setting里面的Secrets里面，添加名为GH,SJH的变量 ，值分别为自己的工号和手机号，不可以空，更不可以不设置。
其余信息均已在代码中写成固定值，比如地点固定为河南省商丘市梁园区商丘学院。


## 三、启用Action
1 点击**Action**，再点击**I understand my workflows, go ahead and enable them**  
2 修改任意文件后提交一次，比如对README.MD文件随便增加一个空格再保存。

## 四、查看运行结果
Actions > auto-report-safe-shangqiuxueyuan > build  
只要全部状态最后都出现√，就表示成功了。
可以在checkin中看详细结果，“上报成功”或者“不能重复上报”。

此后，将会在每天10:00-10:45之间和22:00-22:45之间各报平安一次。  
若有其它需求，可以在[.github/workflows/run.yml]中自行修改
##  如果已经报过平安信息了，就会提示“不能重复上报！”，所以本项目主要是万一忘记上报平安信息了，保底用。
# 千万不要完全交给托管，要对自己的健康安全负责。
