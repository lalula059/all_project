# https://09d3020354aa.com/main
# 很像eval加密，但是又hook不到，虽然最后还是搞出来了，在虚拟机执行的。还是需要去了解它是用什么的
# 用window.onbeforeunload = function () {
#     debugger;
# }
# 进行hook，因为他是修改href，你要么修改property但是不能重定义，所以你找isvip或者hook上面那个