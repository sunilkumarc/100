"use strict"

module.exports = function(sequelize, DataTypes) {
    var Battles = sequelize.define("Battles", {
        name: {
            type: DataTypes.STRING,
            primaryKey: true
        },
        year: {
            type: DataTypes.STRING
        },
        battle_number: {
            type: DataTypes.STRING
        },
        attacker_king: {
            type: DataTypes.STRING
        },
        defender_king: {
            type: DataTypes.STRING
        },
        attacker_1: {
            type: DataTypes.STRING
        },
        attacker_2: {
            type: DataTypes.STRING
        },
        attacker_3: {
            type: DataTypes.STRING
        },
        attacker_4: {
            type: DataTypes.STRING
        },
        defender_1: {
            type: DataTypes.STRING
        },
        defender_2: {
            type: DataTypes.STRING
        },
        defender_3: {
            type: DataTypes.STRING
        },
        defender_4: {
            type: DataTypes.STRING
        },
        attacker_outcome: {
            type: DataTypes.STRING
        },
        battle_type: {
            type: DataTypes.STRING
        },
        major_death: {
            type: DataTypes.STRING
        },
        major_capture: {
            type: DataTypes.STRING
        },
        attacker_size: {
            type: DataTypes.STRING
        },
        defender_size: {
            type: DataTypes.STRING
        },
        attacker_commander: {
            type: DataTypes.STRING
        },
        defender_commander: {
            type: DataTypes.STRING
        },
        summer: {
            type: DataTypes.STRING
        },
        location: {
            type: DataTypes.STRING
        },
        region: {
            type: DataTypes.STRING
        },
        note: {
            type: DataTypes.STRING
        }
    }, {
       tableName: 'battles'
    });

    return Battles;
}
