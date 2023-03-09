## 用户表
```mysql

CREATE TABLE IF NOT EXISTS `users`(
   `id` INT UNSIGNED AUTO_INCREMENT,
   `username` VARCHAR(100) Unique NOT NULL,
   `password_hash` VARCHAR(200) NOT NULL,
   `name` VARCHAR(64),
   `email` VARCHAR(50),
   `phone` VARCHAR(20),
   `organization` VARCHAR(100),NOT NULL,
   `active` Tinyint(1) NOT NULL,
   `role_id` INT UNSIGNED NOT NULL,
   `scores` INT UNSIGNED Default 0 NOT NULL,
   PRIMARY KEY ( `id` )
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
```
    __tablename__ = 'users'  # 自定义数据表的表名
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    name = db.Column(db.String(64))
    email = db.Column(db.String(50))
    phone = db.Column(db.String(20))
    active = db.Column(db.Boolean, default=True, nullable=False)
    scores = db.Column(db.Integer, default=0,nullable=False)

## 角色表
```mysql
CREATE TABLE IF NOT EXISTS `roles`(
   `id` INT UNSIGNED AUTO_INCREMENT,
   `name` VARCHAR(100) Unique NOT NULL,
   PRIMARY KEY ( `id` )
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

```
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), unique=True, nullable=False)

## 插入数据
```mysql
INSERT INTO roles (name)
    VALUES
    ( "manager");

INSERT INTO roles (name)
    VALUES
    ( "normal_user");
```


## 新实体表
    __tablename__ = 'new_entity'  # 自定义数据表的表名
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    create_time = db.Column(db.DateTime, default=datetime.utcnow)
    # status 标识 审核状态 0: 未审核，1: 审核通过， 2: 审核不通过，3： 未提交,4:提交
    status = db.Column(db.Integer,default=0,nullable=False)
    failed_reason = db.Column(db.Text,nullable=True)

    entity_attributes = db.column(db.LargeBinary,nullable=True)
    

    # 外键关联
    upload_user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    review_user_id = db.Column(db.Integer, db.ForeignKey('users.id'),nullable=True)

```mysql
CREATE TABLE IF NOT EXISTS `new_entities`(
   `id` INT UNSIGNED AUTO_INCREMENT,
   `create_time` VARCHAR(100) NOT NULL,
   `status` INT UNSIGNED default 0 NOT NULL,
   `failed_reason` TEXT,
   `entity_attributes` BLOB,
   `upload_user_id` INT UNSIGNED NOT NULL,
   `review_user_id` INT UNSIGNED,
   PRIMARY KEY ( `id` )
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

```

## 训练任务表
```mysql
CREATE TABLE IF NOT EXISTS `task`(
   `id` INT UNSIGNED AUTO_INCREMENT,
   `create_time` VARCHAR(100) NOT NULL,
   `task_status` VARCHAR(200),
   `task_name` VARCHAR(200) NOT NULL,
   `server_ip` VARCHAR(100) NOT NULL,
   `server_port` VARCHAR(100) NOT NULL,
   `task_desc` TEXT,
   `task_model` VARCHAR(200) NOT NULL,
   `task_user_id` INT UNSIGNED,
   `task_rounds` INT UNSIGNED NOT NULL,
   `task_log` VARCHAR(200),
   PRIMARY KEY ( `id` )
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

```
    


## 积分变动记录表 记录用户积分的变化记录
    __tablename__ = 'scores'  # 自定义数据表的表名
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    create_time = db.Column(db.DateTime, default=datetime.utcnow)
    # 积分变动原因/事件,e.g 用户添加了实体
    change_reasons = db.Column(db.Text)
    # 积分变动记录 e.g.“+1”
    change_records = db.Column(db.Text)
    # 外键关联
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
```
CREATE TABLE IF NOT EXISTS `scores`(
   `id` INT UNSIGNED AUTO_INCREMENT,
   `create_time` VARCHAR(100) NOT NULL,
   `change_reasons` VARCHAR(200),
   `change_records` VARCHAR(200),
   `user_id` INT UNSIGNED NOT NULL,
   PRIMARY KEY ( `id` )
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

```


## 训练模型 表

```mysql
CREATE TABLE IF NOT EXISTS `model`(
   `id` INT UNSIGNED AUTO_INCREMENT,
   `create_time` VARCHAR(100) NOT NULL,
   `model_name` VARCHAR(200) NOT NULL,
   `model_desc` TEXT,
   `client_code` VARCHAR(400) NOT NULL,
   `server_code` VARCHAR(400) NOT NULL,
   `model_user_id` INT UNSIGNED,
   PRIMARY KEY ( `id` )
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
```