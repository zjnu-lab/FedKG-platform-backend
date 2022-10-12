## 用户表
```mysql

CREATE TABLE IF NOT EXISTS `users`(
   `id` INT UNSIGNED AUTO_INCREMENT,
   `username` VARCHAR(100) Unique NOT NULL,
   `password_hash` VARCHAR(200) NOT NULL,
   `name` VARCHAR(64),
   `email` VARCHAR(50),
   `phone` VARCHAR(20),
   `active` Tinyint(1) NOT NULL,
   `role_id` INT UNSIGNED NOT NULL,
   PRIMARY KEY ( `id` )
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
```
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=True)
    name = db.Column(db.String(64))
    email = db.Column(db.String(50))
    phone = db.Column(db.String(20))
    active = db.Column(db.Boolean, default=True, nullable=False)

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
    
