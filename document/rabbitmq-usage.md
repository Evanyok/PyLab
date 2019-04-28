1. installation of rabbitmq
    * install brew
        <p>
        <code>
            $ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
        </code>
        <p>
    * install rabbitmq
        <p>
        <code>
            $ brew install rabbitmq
        </code>
        </p>
2. start rabbitmq, default port is 5462
    <p>
    <code>
        $ brew services start rabbitmq
    </code>
    </p>

3. setting up rabbitmq
    <p>
    <code>
        $ sudo rabbitmqctl add_user myuser mypassword
    </code>
    </p>
    <p>
    <code>
        $ sudo rabbitmqctl set_user_tags myuser administrator
    </code>
    </p>
    <p>
    <code>
        $ sudo rabbitmqctl add_vhost myvhost
    </code>
    </p>
    <p>
    <code>
        $ sudo rabbitmqctl set_permissions -p myvhost myuser ".*" ".*" ".*"
    </code>
    </p>
    <p>
    <code>
        $ sudo scutil --set HostName myhost.local
    </code>
    </p>

4. check status
    <p>
    <code>
        $ sudo rabbitmqctl status
    </code>
    </p>

5. stop rabbitmq
    <p>
    <code>
        $ brew services stop rabbitmq
    </code>
    </p>
