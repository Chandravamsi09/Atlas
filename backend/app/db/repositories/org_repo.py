from typing import Optional, List
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from backend.app.db.repositories.base_repo import BaseRepository
from backend.app.models.organization import Organization, OrgMembership


class OrganizationRepository(BaseRepository[Organization]):
    def __init__(self, db: AsyncSession):
        super().__init__(Organization, db)

    async def get_by_slug(self, slug: str) -> Optional[Organization]:
        stmt = select(Organization).where(Organization.slug == slug.lower())
        result = await self.db.execute(stmt)
        return result.scalar_one_or_none()

    async def get_user_organizations(self, user_id: str) -> List[Organization]:
        stmt = select(Organization).join(OrgMembership).where(OrgMembership.user_id == user_id)
        result = await self.db.execute(stmt)
        return list(result.scalars().all())
