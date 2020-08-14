import Mock from 'mockjs'

var {TeamList} = Mock.mock({
    'TeamList|4-8': [
        {
            "id":"@increment()",
            "name":'@ctitle(4,7)',
            "personList|50-100":{
                "name":'@cname()',
            },
            "owner":'@cname()',
            "time":'@date(yyyy/MM/dd hh:mm:ss)',
            "introduction":'@cparagraph(5,50)'
        }
    ]
})
var {MessageList} = Mock.mock({
    'MessageList|8-10': [
        {
            "id":"@increment()",
            "MessageTitle":'@ctitle(7,15)',
            "date":'@date(yyyy/MM/dd hh:mm:ss)',
            "MessageContent":'@cparagraph(5,50)'
        }
    ]
})
Mock.mock('/api/post/messagelist','post',(options)=>{
    return{
        status:200,
        message:'获取消息列表成功',
        MessageList:MessageList,
        total: MessageList.length
    }
})
Mock.mock('/api/post/teamlist','post',(options)=>{
    return{
        status:200,
        message:'获取团队列表成功',
        sideData:TeamList,
        total: TeamList.length
    }
})
Mock.mock('api/post/add/Team','post',(options)=>{
    const body = JSON.parse(options.body)
    TeamList.push(Mock.mock({
        "id":"@increment()",
            "name":body.name,
            "personList|50-100":{
                "name":'@cname()',
            },
            "owner":body.owner,
            "time":body.time,
            "introduction":body.introduction
    }))
    return{
        status:200,
        message:'添加成功',
        sideData:TeamList,
        total: TeamList.length
    }
})