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

    
