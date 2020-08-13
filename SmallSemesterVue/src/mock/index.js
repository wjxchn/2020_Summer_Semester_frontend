import Mock from 'mockjs'

const {TeamList} = Mock.mock({
    'TeamList|4-8': [
        {
            "id":"@increment()",
            "name":'@ctitle(4,7)',
            "personList|50-100":{
                "name":'@cname()',

            },
            "owner":'@cname()',
            "time":'@date(yyyy/MM/dd hh:mm:ss)'
        }
    ]
})
Mock.mock('/api/post/teamlist','post',()=>{
    return{
        status:200,
        message:'获取团队列表成功',
        sideData:TeamList,
        total: TeamList.length
    }
})