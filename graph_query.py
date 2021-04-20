#graph ql

#Resources

#https://juejin.cn/post/6844903457053212685
#https://github.com/zhouyuexie/learn-graphql

{
 echo(message:"world")
}

query echo {
    echo(message: "world test")
}

query{
  getFirstPost{title}
}

query{
  getFirstPost{
  title,
  content,
  category}
}
