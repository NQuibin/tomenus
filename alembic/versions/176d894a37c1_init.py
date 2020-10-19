"""init

Revision ID: 176d894a37c1
Revises: 
Create Date: 2020-10-18 18:36:56.545009

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = '176d894a37c1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('restaurants',
        sa.Column('id', sqlalchemy_utils.types.uuid.UUIDType(), nullable=False),
        sa.Column('name', sa.String(length=128), nullable=False),
        sa.Column('primary_category', sa.String(length=128), nullable=False),
        sa.Column('area', sa.String(length=64), nullable=False),
        sa.Column('description', sa.Text(), nullable=True),
        sa.Column('address1', sa.String(length=128), nullable=True),
        sa.Column('address2', sa.String(length=28), nullable=True),
        sa.Column('city', sa.String(length=128), nullable=True),
        sa.Column('province', sa.String(length=64), nullable=True),
        sa.Column('postal_code', sa.String(length=16), nullable=True),
        sa.Column('country', sa.String(length=64), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint('id', name=op.f('restaurants_pkey'))
    )
    op.create_table('menus',
        sa.Column('id', sqlalchemy_utils.types.uuid.UUIDType(), nullable=False),
        sa.Column('restaurant_id', sqlalchemy_utils.types.uuid.UUIDType(), nullable=True),
        sa.Column('name', sa.String(length=64), nullable=False),
        sa.Column('description', sa.Text(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(['restaurant_id'], ['restaurants.id'], name=op.f('fk_menus_restaurant_id_restaurants')),
        sa.PrimaryKeyConstraint('id', name=op.f('menus_pkey'))
    )
    op.create_table('menu_items',
        sa.Column('id', sqlalchemy_utils.types.uuid.UUIDType(), nullable=False),
        sa.Column('menu_id', sqlalchemy_utils.types.uuid.UUIDType(), nullable=True),
        sa.Column('name', sa.String(length=64), nullable=False),
        sa.Column('section', sa.String(length=128), nullable=False),
        sa.Column('section_order', sa.Integer(), nullable=False),
        sa.Column('order', sa.Integer(), nullable=False),
        sa.Column('description', sa.Text(), nullable=True),
        sa.Column('price', sa.Integer(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(['menu_id'], ['menus.id'], name=op.f('fk_menu_items_menu_id_menus')),
        sa.PrimaryKeyConstraint('id', name=op.f('menu_items_pkey'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('menu_items')
    op.drop_table('menus')
    op.drop_table('restaurants')
    # ### end Alembic commands ###