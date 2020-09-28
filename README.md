# THU-CST-PEX

The corse-selection tool for THU Physic Experiment

This is an easy tool written by Python.

> 编号对应表：
>  2 准稳态法测导热系数和比热 
>  3 弹簧振子实验 
>  5 透镜焦距的测定 
>  6 三线摆和扭摆
>  9 示波器的原理和使用
>  10 阻尼振动与受迫振动
>  12 空气热容比的测量
>  13 弹性模量的测量、动力学法测杨氏模量
>  14 用传感器测空气相对压力系数
>  15 直流电桥测电阻
>  16 分光计的调节和色散曲线的测定
>  17 电学元件伏安特性的测量
>  18 液体粘度的测量
>  19 灵敏电流计
>  20 弦振动实验

重要：
本程序的SUCCESS输出**不**代表抢课成功，仅代表成功向服务器发送了选课请求！
如果你上周（指还没有切换时的那一周）已经抢到课，请将该课程信息加入payload中，否则该选课会失效！
VITAL
THE OUTPUT "SUCCESS" WHEN RUNNING python qiangke.py DID **NOT** SHOW THAT YOU HAVE GOT THE COURSE BUT ONLY SHOWS THAT YOU HAVE SUCCESSFULLY SENT A MESSAGE TO THE HOST.
IF YOU HAVE CHOSEN A COURSE SUCCESSFULLY LAST WEEK, PLEASE ADD THE RELEVANT INFORMATION TO PAYLOAD, OTHERWISE, THE COURSE SELECTION WILL FAIL!

使用说明：

To use this tool, you shall first lauch into the website and get your cookies. You are recommended to accomplish the step by Chrome.
Note: The cookies may be CHANGED in just a few hours so check it before your course selection.

Then change the blank in the qiangke.py with your cookie and your preferred lessons.

Do not forget to kill the python mission by task manager to stop the process.
请务必使用任务管理器杀进程或者关机！否则会导致严重后果！本工具的使用事件一般不得超过2分钟。2分钟后如确是仍需使用，请至少在任务管理器中找到位于最上方的PYTHON进程并关闭之。

Eg:
周一下午 灵敏电流计 19=12
周三晚上 液体粘度的测量 18=33
退课 直流电桥测电阻 15=0

Enjoy yourself!
