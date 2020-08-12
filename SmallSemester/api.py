from django.http import JsonResponse,HttpResponse
import json
from SmallSemesterChild.models import Test, Plain, Test3, Group, Document, Comment, Demo, Browse, Belong, Favorite
from SmallSemesterChild import models
from SmallSemester import settings,token
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.db.models.query import EmptyQuerySet
from django.db.models import Max
def ajax_list(request):
    a = list(range(100))
    return JsonResponse(a, safe=False)

def ajax_dict(request):
    name_dict = {'twz': 'Love python and Django', 'zqxt': 'I am teaching Django'}
    return JsonResponse(name_dict)

def addname(request):
    if request.method == 'POST':
        request_data = request.body
        print(request_data)
        request_dict = json.loads(request_data.decode('utf-8'))
        postname = request_dict.get('inname')
        print(postname)
        test1 = Test(name = postname)
        test1.save()
        ret_dict = {'code': 200, 'msg': "填写信息成功"}
        return JsonResponse(ret_dict)
    else:
        ret_dict = {'code': 400, 'msg': "填写信息失败"}
        return JsonResponse(ret_dict)

def getname(request):
    if request.method == 'POST':
        request_data_get = request.body
        print(request_data_get)
        request_dict_get = json.loads(request_data_get.decode('utf-8'))
        getpostname = request_dict_get.get('queryname')
        print(getpostname)
        test2 = models.Test.objects.filter(name__contains = getpostname)
        print(test2)
        for item in test2:
            print(item.name)
        ret_getdict = {'code': 200, 'msg': "查询成功"}
        return JsonResponse(ret_getdict)
    else:
        ret_getdict = {'code': 400, 'msg': "查询失败"}
        return JsonResponse(ret_getdict)        

def addplaintext(request):
    if request.method == 'POST':
        request_data = request.body
        print(request_data)
        request_dict = json.loads(request_data.decode('utf-8'))
        postname = request_dict.get('content')
        print(postname)
        test3 = Plain(plainname = postname)
        test3.save()
        ret_dict = {'code': 200, 'msg': "填写富文本成功"}
        return JsonResponse(ret_dict)
    else:
        ret_dict = {'code': 400, 'msg': "填写富文本失败"}
        return JsonResponse(ret_dict)

def getplaintext(request):
    if request.method == 'GET':
        test4 = models.Plain.objects.last()
        print(test4.plainname)
        ret_dict = {'code': 200, 'msg': "显示富文本成功", 'content': test4.plainname}
        return JsonResponse(ret_dict)
    else:
        ret_dict = {'code': 400, 'msg': "显示富文本失败", 'content': ''}
        return JsonResponse(ret_dict)

def uploadfile(request):
    #获取文件
    infile = request.FILES.get("file")
    #创建文件
    save_path ="%s/%s" % (settings.MEDIA_ROOT,infile.name)
    print(save_path)
    with open(save_path, "wb") as f:
        #将文件以二进制形式写入到指定路径
        for temp in infile.chunks():
            f.write(temp)
    ret_dict = {'code': 200, 'msg': "上传成功"}
    return JsonResponse(ret_dict)

def downloadfile(request):
    save_path ="%s/%s" % (settings.MEDIA_ROOT,'testphoto.jpg')
    file = open(save_path, 'rb')
    response = HttpResponse(file)
    response['Content-Type'] = 'application/octet-stream' #设置头信息，告诉浏览器这是个文件
    response['Content-Disposition'] = 'attachment;filename="testphoto.jpg"'
    return response

def sendemail(request):
    msg='<a href="http://localhost:8000/home" target="_blank">点击激活</a>'
    send_mail('注册激活','','2424773081@qq.com', ['14798065468@163.com'], html_message=msg)
    ret_dict = {'code': 200, 'msg': "发送邮件成功"}
    return JsonResponse(ret_dict)

def createuser(request):
    request_data = request.body
    request_dict = json.loads(request_data.decode('utf-8'))
    username = request_dict.get('username')
    password = request_dict.get('password')
    email = request_dict.get('email')
    checkuser = models.User.objects.filter(username = username)
    if checkuser.exists():
        ret_dict = {'code': 400, 'msg': "用户已存在"}
        return JsonResponse(ret_dict)        
    else:       
        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()
        ret_dict = {'code': 200, 'msg': "创建用户成功"}
        return JsonResponse(ret_dict)
 
def login(request):
    request_data = request.body
    request_dict = json.loads(request_data.decode('utf-8'))
    username = request_dict.get('username')
    password = request_dict.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        ret_dict = {'code': 200, 'msg': "登录成功"}
        return JsonResponse(ret_dict)            
    else:
        ret_dict = {'code': 400, 'msg': "账号或密码错误"}
        return JsonResponse(ret_dict)

def changepassword(request):
    request_data = request.body
    request_dict = json.loads(request_data.decode('utf-8'))
    username = request_dict.get('username')
    oldpassword = request_dict.get('oldpassword')
    newpassword = request_dict.get('newpassword')
    user = authenticate(username=username, password=oldpassword)
    if user is not None:
        u = User.objects.get(username = username)
        u.set_password(newpassword)
        u.save()
        ret_dict = {'code': 200, 'msg': "修改密码成功"}
        return JsonResponse(ret_dict)
    else:
        ret_dict = {'code': 400, 'msg': "修改密码失败"}
        return JsonResponse(ret_dict)

def verifyuser(request):
    request_data = request.body
    request_dict = json.loads(request_data.decode('utf-8'))
    username = request_dict.get('username')
    password = request_dict.get('password')
    authuser = authenticate(username=username, password=password)
    if authuser is not None:
        user = models.User.objects.get(username = username)
        to_email = user.email
        mail_title = "激活邮件"
        msg='<p>您已收到激活邮件，注册账号成功，账号可以使用了。</p><a href="http://localhost:8000/home" target="_blank">点击进入首页</a>'
        send_status = send_mail(mail_title,'','2424773081@qq.com', [to_email], html_message=msg)
        if send_status:
            user.is_active = 1
            user.save()            
            ret_dict = {'code': 200, 'msg': "发送激活邮件成功"}
            return JsonResponse(ret_dict)
        else:
            ret_dict = {'code': 400, 'msg': "发送激活邮件失败"}
            return JsonResponse(ret_dict)
    else:
        ret_dict = {'code': 401, 'msg': "账号或密码错误"}
        return JsonResponse(ret_dict)

def show_personalintro(request):
    if request.method == 'POST':
        request_data = request.body
        print(request_data)
        request_dict = json.loads(request_data.decode('utf-8'))

        username = request_dict.get('username')
        user = models.User.objects.get(username = username)
        user_dict = {'username': user.username, 'email': user.email}
        return JsonResponse(user_dict)
    else:
        ret_dict = {'code': 400, 'msg': "查看个人信息失败"}
        return JsonResponse(ret_dict)

def change_personalintro(request):
    if request.method == 'POST':
        request_data = request.body
        print(request_data)
        request_dict = json.loads(request_data.decode('utf-8'))

        username = request_dict.get('username')
        email = request_dict.get('email')
        user = models.User.objects.get(username = username)
        user.email = email
        user.save()

        ret_dict = {'code': 200, 'msg': "修改个人信息成功"}
        return JsonResponse(ret_dict)
    else:
        ret_dict = {'code': 400, 'msg': "修改个人信息失败"}
        return JsonResponse(ret_dict)    

def show_personal_doc(request):
    if request.method == 'POST':
        request_data = request.body
        print(request_data)
        request_dict = json.loads(request_data.decode('utf-8'))
        
        docid = request_dict.get('doc_id')
        username = request_dict.get('username')
        doc = Document.objects.get(doc_id = docid)
        doc_dict = {'docid': doc.doc_id, 'doc_name': doc.doc_name, 'doc_creater': doc.doc_creater, 'doc_intro': doc.introduction, 'doc_content': doc.doc_content}

        browse_object = Browse.objects.all().aggregate(Max('browse_id'))
        if browse_object.exists():
            browse_id = browse_object.browse_id + 1
        else:
            browse_id = 0
        
        browse = Browse(browse_id = browse_id, username = username, doc_id = docid)
        browse.save()

        return JsonResponse(doc_dict)
    else:
        ret_dict = {'code': 400, 'msg': "查看文档失败"}
        return JsonResponse(ret_dict)

def change_personal_doc(request):
    if request.method == 'POST':
        request_data = request.body
        print(request_data)
        request_dict = json.loads(request_data.decode('utf-8'))

        docid = request_dict.get('doc_id')
        docname = request_dict.get('doc_name')
        doccreater = request_dict.get('doc_creater')
        docintro = request_dict.get('doc_intro')
        doccontent = request_dict.get('doc_content')

        doc = Document.objects.get(doc_id = docid)

        doc.doc_name = docname
        doc.doc_creater = doccreater
        doc.introduction = docintro
        doc.doc_content = doccontent

        doc.save()

        ret_dict = {'code': 200, 'msg': "修改文档成功"}
        return JsonResponse(ret_dict)
    else:
        ret_dict = {'code': 400, 'msg': "修改文档失败"}
        return JsonResponse(ret_dict)

def add_personal_doc(request):
    if request.method == 'POST':
        request_data = request.body
        print(request_data)
        request_dict = json.loads(request_data.decode('utf-8'))
        doc_content = request_dict.get('content')
        doc_name = request_dict.get('doc_name')
        introduction = request_dict.get('introduction')
        doc_creater = request_dict.get('doc_creater')
        isin_recycle = False 
        doc_object = Document.objects.all().aggregate(Max('doc_id'))

        if doc_object.exists():
            doc_id = doc_object.doc_id + 1
        else:
            doc_id = 0
            
        doc = Document(doc_name=doc_name, doc_id=doc_id, doc_content=doc_content, introduction=introduction, doc_creater=doc_creater, isin_recycle=isin_recycle)
        doc.save()
        
        ret_dict = {'code': 200, 'msg': "上传个人文档成功"}
        return JsonResponse(ret_dict)
    else:
        ret_dict = {'code': 400, 'msg': "上传个人文档失败"}
        return JsonResponse(ret_dict)

def create_group(request):
    if request.method == 'POST':
        request_data = request.body
        print(request_data)
        request_dict = json.loads(request_data.decode('utf-8'))

        creater = request_dict.get('creater')
        name = request_dict.get('name')
        introduction = request_dict.get('introduction')

        group_object = Group.objects.all().aggregate(Max('doc_groupid'))
        if group_object.exists():
            groupid = group_object.groupid + 1
        else:
            groupid = 0
        group = Group(group_name = name, creater = creater, introduction = introduction, doc_groupid = groupid)
        group.save()
        ret_dict = {'code': 200, 'msg': "创建团队成功"}
        return JsonResponse(ret_dict)
    else:
        ret_dict = {'code': 400, 'msg': "创建团队失败"}
        return JsonResponse(ret_dict)

def add_group_doc(request):
    if request.method == 'POST':
        request_data = request.body
        print(request_data)
        request_dict = json.loads(request_data.decode('utf-8'))

        groupid = request_dict.get('groupid')
        docid = request_dict.get('docid')
        document_object = Document.objects.get(doc_id = docid)
        if document_object.exists():
            document_object.doc_groupid = groupid
            document_object.save()
            ret_dict = {'code': 200, 'msg': "添加团队文档成功"}
            return JsonResponse(ret_dict)
        else:
            ret_dict = {'code': 400, 'msg': "添加团队文档失败"}
            return JsonResponse(ret_dict)
    else:
        ret_dict = {'code': 400, 'msg': "添加团队文档失败"}
        return JsonResponse(ret_dict)

def delete_personal_doc(request):
    if request.method == 'POST':
        request_data = request.body
        print(request_data)
        request_dict = json.loads(request_data.decode('utf-8'))

        docid = request_dict.get('docid')
        document_object = Document.objects.get(doc_id = docid)
        if document_object.exists():
            document_object.delete()
            ret_dict = {'code': 200, 'msg': "删除个人文档成功"}
            return JsonResponse(ret_dict)
        else:
            ret_dict = {'code': 400, 'msg': "删除个人文档失败"}
            return JsonResponse(ret_dict)
    else:
        ret_dict = {'code': 400, 'msg': "删除个人文档失败"}
        return JsonResponse(ret_dict)

def delete_group_doc(request):
    if request.method == 'POST':
        request_data = request.body
        print(request_data)
        request_dict = json.loads(request_data.decode('utf-8'))

        docid = request_dict.get('docid')
        document_object = Document.objects.get(doc_id = docid)
        if document_object.exists():
            document_object.doc_groupid = 'null'
            document_object.save()
            ret_dict = {'code': 200, 'msg': "删除团队文档成功"}
            return JsonResponse(ret_dict)
        else:
            ret_dict = {'code': 400, 'msg': "删除团队文档失败"}
            return JsonResponse(ret_dict)
    else:
        ret_dict = {'code': 400, 'msg': "删除团队文档失败"}
        return JsonResponse(ret_dict)

def take_doc_to_recycle(request):
    if request.method == 'POST':
        request_data = request.body
        print(request_data)
        request_dict = json.loads(request_data.decode('utf-8'))

        docid = request_dict.get('docid')
        document_object = Document.objects.get(doc_id = docid)
        if document_object.exists():
            document_object.isin_recycle = False
            document_object.save()
            ret_dict = {'code': 200, 'msg': "删除个人文档成功"}
            return JsonResponse(ret_dict)
        else:
            ret_dict = {'code': 400, 'msg': "删除个人文档失败"}
            return JsonResponse(ret_dict)
    else:
        ret_dict = {'code': 400, 'msg': "删除个人文档失败"}
        return JsonResponse(ret_dict)
    
def recover_from_recycle(request):
    if request.method == 'POST':
        request_data = request.body
        print(request_data)
        request_dict = json.loads(request_data.decode('utf-8'))
        
        docid = request_dict.get('docid')
        document_object = Document.objects.get(doc_id = docid)
        if document_object.exists():
            document_object.isin_recycle = True
            document_object.save()
            ret_dict = {'code': 200, 'msg': "恢复文件成功"}
            return JsonResponse(ret_dict)
        else:
            ret_dict = {'code': 400, 'msg': "恢复文件文档失败"}
            return JsonResponse(ret_dict)
    else:
        ret_dict = {'code': 400, 'msg': "恢复失败"}
        return JsonResponse(ret_dict)

def delete_from_recycle(request):
    if request.method == 'POST':
        request_data = request.body
        print(request_data)
        request_dict = json.loads(request_data.decode('utf-8'))

        docid = request_dict.get('docid')
        document_object = Document.objects.get(doc_id = docid)
        if document_object.exists():
            document_object.delete()
            ret_dict = {'code': 200, 'msg': "删除回收站文档成功"}
            return JsonResponse(ret_dict)
        else:
            ret_dict = {'code': 400, 'msg': "文件未找到"}
            return JsonResponse(ret_dict)
    else:
        ret_dict = {'code': 400, 'msg': "删除回收站文档失败"}
        return JsonResponse(ret_dict)

def show_personal_doclist(request):
    if request.method == 'POST':
        request_data = request.body
        print(request_data)
        request_dict = json.loads(request_data.decode('utf-8'))

        username = request_dict.get('username')
        doclist = Document.objects.filter(doc_creater=username)

        alist = []
        for doc in doclist:
            alist.append({'docid':doc.doc_id,'docname':doc.doc_name,'createtime':doc.time})
        return JsonResponse(alist)
    else:
        ret_dict = {'code': 400, 'msg': "个人文档页面加载失败"}
        return JsonResponse(ret_dict)

def show_favorite_doclist(request):
    if request.method == 'POST':
        request_data = request.body
        print(request_data)
        request_dict = json.loads(request_data.decode('utf-8'))

        username = request_dict.get('username')
        doclist = Favorite.objects.filter(username = username)

        alist = []
        for doct in doclist:
            doc = Document.objects.get(doc_id = doct.doc_id)
            alist.append({'docid': doc.doc_id, 'docname': doc.doc_name, 'createtime': doc.time}) 
        return JsonResponse(alist)
    else:
        ret_dict = {'code': 400, 'msg': "收藏文档页面加载失败"}
        return JsonResponse(ret_dict)

def show_group_doclist(request):
    if request.method == 'POST':
        request_data = request.body
        print(request_data)
        request_dict = json.loads(request_data.decode('utf-8'))

        groupid = request_dict.get('doc_groupid')
        doclist = Document.objects.filter(doc_groupid=groupid)

        alist = []
        for doc in doclist:
            alist.append({'docid':doc.doc_id,'docname':doc.doc_name,'createtime':doc.time})
        return JsonResponse(alist)
    else:
        ret_dict = {'code': 400, 'msg': "团队文档页面加载失败"}
        return JsonResponse(ret_dict)

def leave_group(request):
    if request.method == 'POST':
        request_data = request.body
        print(request_data)
        request_dict = json.loads(request_data.decode('utf-8'))

        username = request_dict.get('username')
        groupid =  request_dict.get('doc_groupid')
        belong = Belong.objects.filter(username=username)
        group = Group.objects.filter(doc_groupid=groupid)

        if username!=group.creater:
            belong.delete()
            ret_dict = {'code': 200, 'msg': "退出团队成功"}
            return JsonResponse(ret_dict)
        else:
            ret_dict = {'code': 400, 'msg': "该用户为小组创建者，不可退出"}
            return JsonResponse(ret_dict)
    else:
        ret_dict = {'code': 400, 'msg': "退出团队失败"}
        return JsonResponse(ret_dict)
        
def dismiss_group(request):
    if request.method == 'POST':
        request_data = request.body
        print(request_data)
        request_dict = json.loads(request_data.decode('utf-8'))

        username = request_dict.get('username')
        groupid =  request_dict.get('doc_groupid')
        group = Group.objects.filter(doc_groupid=groupid)
        belonglist = Belong.objects.filter(groupid=groupid)
        if username==group.creater:
            group.delete()
            belonglist.delete()
            ret_dict = {'code': 200, 'msg': "解散团队成功"}
            return JsonResponse(ret_dict)
        else:
            ret_dict = {'code': 400, 'msg': "该用户不是小组创建者，不可解散团队"}
            return JsonResponse(ret_dict)
    else:
        ret_dict = {'code': 400, 'msg': "退出团队失败"}
        return JsonResponse(ret_dict)

def join_group(request):
    if request.method == 'POST':
        request_data = request.body
        print(request_data)
        request_dict = json.loads(request_data.decode('utf-8'))

        username = request_dict.get('username')
        groupid =  request_dict.get('groupid')

        belong = Belong(username=username, group_id=groupid)
        belong.save()
        ret_dict = {'code': 200, 'msg': "加入团队成功"}
        return JsonResponse(ret_dict)
    else:
        ret_dict = {'code': 400, 'msg': "加入团队失败"}
        return JsonResponse(ret_dict)

def show_grouplist(request):
    if request.method == 'POST':
        request_data = request.body
        print(request_data)
        request_dict = json.loads(request_data.decode('utf-8'))

        username = request_dict.get('username')
        belong_list = Belong.objects.filter(username=username)
        group_name_list=[]
        for belong in belong_list:
            group = Group.objects.get(groupid=belong.groupid)
            group_name_list.append({'group_name':group.group_name})
        return JsonResponse(group_name_list)
    else:
        ret_dict = {'code': 400, 'msg': "显示团队列表"}
        return JsonResponse(ret_dict)

def favorite_doc(request):
    if request.method == 'POST':
        request_data = request.body
        print(request_data)
        request_dict = json.loads(request_data.decode('utf-8'))

        username = request_dict.get('username')
        doc_id = request_dict.get('doc_id')
        favorite = Favorite(doc_id=doc_id, username=username)
        favorite.save()
        ret_dict = {'code': 200, 'msg': "收藏成功"}
        return JsonResponse(ret_dict)
    else:
        ret_dict = {'code': 400, 'msg': "收藏失败"}
        return JsonResponse(ret_dict)

def delete_group_member(request):
    if request.method == 'POST':
        request_data = request.body
        print(request_data)
        request_dict = json.loads(request_data.decode('utf-8'))

        usernameA = request_dict.get('usernameA')  #团队创建者
        usernameB = request_dict.get('usernameB')  #被删除者
        groupid = request_dict.get('groupid')
        group = Group.objects.get(groupid=groupid)
        if usernameA == group.creater:
            Belong.objects.fliter(username=usernameB,groupid=groupid).delete()
            ret_dict = {'code': 200, 'msg': "踢出团队成功"}
            return JsonResponse(ret_dict)
        else:
            ret_dict = {'code': 400, 'msg': "非团队管理员无权限踢出团队"}
            return JsonResponse(ret_dict)
    else:
        ret_dict = {'code': 400, 'msg': "踢出团队失败"}
        return JsonResponse(ret_dict)

def add_comment(request):
    if request.method == 'POST':
        request_data = request.body
        print(request_data)
        request_dict = json.loads(request_data.decode('utf-8'))

        username = request_dict.get('username')
        content = request_dict.get('content')
        doc_id = request_dict.get('doc_id')
        comment_object = Commnet.objects.all().aggregate(Max('comment_id'))

        if comment_object.exists():
            comment_id = comment_object.comment_id + 1
        else:
            comment_id = 0
        comment = Comment(com_content=content, com_author=username, doc_id=doc_id, com_id=comment_id)
        comment.save()
        ret_dict = {'code': 200, 'msg': "添加评论成功"}
        return JsonResponse(ret_dict)
    else:
        ret_dict = {'code': 400, 'msg': "添加评论失败"}
        return JsonResponse(ret_dict)

def return_demo(request):
    if request.method == 'POST':
        request_data = request.body
        print(request_data)
        request_dict = json.loads(request_data.decode('utf-8'))

        demo_id = request_dict.get('demo_id')
        demo = Demo.objects.get(demo_id=demo_id)
        ret_dict = {'code': 200, 'msg': "返回模板成功", 'content':demo.demo_content}
        return JsonResponse(ret_dict)
    else:
        ret_dict = {'code': 400, 'msg': "返回模板失败"}
        return JsonResponse(ret_dict)

def latest_browse(request):
    if request.method == 'POST':
        request_data = request.body
        print(request_data)
        request_dict = json.loads(request_data.decode('utf-8'))
        username = request_dict.get('username')
        browse = Browse.objects.all().filter(username=username).aggregate(Max('browse_time'))
        doc = Document.objects.get(doc_id=browse.doc_id)
        ret_dict = {'code': 200, 'msg': "返回最后浏览成功", 'content':doc.doc_content, 'doc_id':doc.doc_id, 'time':doc_time, 'doc_id':doc.doc_name, 'doc_creater':doc.doc_creater}
        return JsonResponse(ret_dict)
    else:
        ret_dict = {'code': 400, 'msg': "返回最后浏览失败"}
        return JsonResponse(ret_dict)
