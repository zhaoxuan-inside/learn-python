INSERT INTO user (username, password)
VALUES
('test', 'scrypt:32768:8:1$Tfd2SRrHou9k0K8F$c791d5742a674ff66336839eb42bc2d40f3331e7c3bbd98e0506a1049acb27d27d0f8ec2a94a96bc7571a8c1d05d6d64269f4cce9c181044ce8500bb91aecc8f'),
('other', 'scrypt:32768:8:1$QV3CU1N1RYYsDRk7$c049bc067044b203ff9f6cdea96ae77322723336df2cbedd53a8548bd7ae3c7d38f3ce5f714af11c4b3365b79d2aaf2a50168e8b49c0e3d236975d398fd08eab');

INSERT INTO post (title, body, author_id)
VALUES
('test title', 'test' || x'0a' || 'body', 1);