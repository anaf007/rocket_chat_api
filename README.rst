flask集成Rocket.Chat聊天框架的api调用提供
====================================================================

the flask rocket.chat，


快速开始
------------------------------------------------------------------

::

    git clone https://github.com/anngle/rockat_chat_api
    cd rockat_chat_api
    pip install -r requirements/dev.txt
    cp .env.example .env
    npm install
    npm start  


::

    flask db init
    flask db migrate
    flask db upgrade
    npm start


部署
------------------------------------------------------------------

::

    export FLASK_ENV=production
    export FLASK_DEBUG=0
    export DATABASE_URL="<YOUR DATABASE URL>"
    npm run build   # build assets with webpack
    flask run       # start the flask server

