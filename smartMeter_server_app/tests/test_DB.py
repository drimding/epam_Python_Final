from smartMeter_server_app import db
from smartMeter_server_app.models.home_model import Home
from smartMeter_server_app.schemas.home_schema import HomeSchema
from smartMeter_server_app.service.home_service import HomeService
from smartMeter_server_app.service.user_service import UserService

if __name__ == '__main__':
    user = UserService.get_bu_username('user2')
    print(user)
    print(user.homes)
    print(HomeService.get_all_by_current_user(user))
    print()

    homeSchema = HomeSchema()
    home = homeSchema.load({"home_name": "test Name",
                            "address": "test_address", "user_id": user.id}, session=db.session)
   # HomeService.add(home)
    print(home)
    print(HomeService.get_by_uuid('49e9aae7-10a8-4ac2-9e9e-8600cef28252'))
