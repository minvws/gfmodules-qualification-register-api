from app.db.db_session import DbSession
from app.db.entities.vendor import Vendor
from app.db.repository.repository_base import RepositoryBase


class VendorRepository(RepositoryBase[Vendor]):

    model = Vendor

    def __init__(self, db_session: DbSession):
        super().__init__(db_session)
