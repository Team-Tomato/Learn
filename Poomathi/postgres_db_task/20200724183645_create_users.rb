class CreateUsers < ActiveRecord::Migration[6.0]
  def change
    create_table :users do |t|
      t.string :name, null: false
      t.string :email, null: false
      t.string :phone_no, null: false
      t.string :state, null: false
      t.string :city, null: false
      t.string :pincode, null: false

      t.timestamps
    end
    add_index :users, :email, unique: true
  end
end
