//
//  ViewController.swift
//  Gem Clicker 2
//
//  Created by Ayush on 4/13/19.
//  Copyright © 2019 Glinium. All rights reserved.
//

import UIKit

struct localStorage {
    static let gemsKey = "gems"
    static let drillInfoKey = "drillInfo"
    static let currentGemTypeKey = "currentGemType"
    static let nextGemTypeKey = "nextGemType"
}

struct gemTypes {
    static let topaz = ["name": "Topaz", "cost": "0", "image": "topaz.png"]
    static let sapphire = ["name": "Sapphire", "cost": "1500", "image": "sapphire.png"]
    static let emerald = ["name": "Emerald", "cost": "5000", "image": "emerald.png"]
    static let ruby = ["name": "Ruby", "cost": "8000", "image": "ruby.png"]
    static let aquamarine = ["name": "Aquamarine", "cost": "15000", "image": "aquamarine.png"]
    static let diamond = ["name": "Diamond", "cost": "25500", "image": "diamond.png"]
}

let defaults = UserDefaults.standard
let drillInfoDefault = ["drill": 0, "autoDrill": 0, "titaniumDrill": 0, "fireDrill": 0]
let currentGemTypeDefault = gemTypes.topaz
let nextGemTypeDefault = gemTypes.sapphire

var drillInfo = drillInfoDefault
var gems = 0
var currentGemType = gemTypes.topaz
var nextGemType = gemTypes.sapphire


func startup() {
    gems = defaults.integer(forKey: localStorage.gemsKey)
    drillInfo = defaults.dictionary(forKey: localStorage.drillInfoKey) as? [String: Int] ?? drillInfoDefault
    currentGemType = defaults.dictionary(forKey: localStorage.currentGemTypeKey) as? [String: String] ?? currentGemTypeDefault
    nextGemType = defaults.dictionary(forKey: localStorage.nextGemTypeKey) as? [String: String] ?? nextGemTypeDefault
}

func main() {
    
    func store() {
        Canvas.shared.clear()
        
        let backText = Text(string: "Back", fontSize: 50.0, fontName: "Copperplate", color: #colorLiteral(red: 0.2392156869, green: 0.6745098233, blue: 0.9686274529, alpha: 1))
        backText.center.y = 38
        backText.center.x = 25
        
        var buyGemText2 = Text(string: "Buy New Gem: ", fontSize: 60.0, fontName: "Copperplate", color: #colorLiteral(red: 0.2392156869, green: 0.6745098233, blue: 0.9686274529, alpha: 1))
        buyGemText2.center.y = 30
        buyGemText2.center.x = 0
        
        var buyGemText = Text(string: String(nextGemType["name"] ?? "") +
            " for " + String(nextGemType["cost"] ?? "") + " gems", fontSize: 60.0, fontName: "Copperplate", color: #colorLiteral(red: 0.2392156869, green: 0.6745098233, blue: 0.9686274529, alpha: 1))
        buyGemText.center.y = 25
        buyGemText.center.x = 0
        
        let divider = Line(start: Point(x: 28, y: 19.3), end: Point(x: -28, y: 19.3))
        divider.color = #colorLiteral(red: 0.4745098054, green: 0.8392156959, blue: 0.9764705896, alpha: 1)
        
        var buyDrillText = Text(string: "Buy drill", fontSize: 51.0, fontName: "Copperplate", color: #colorLiteral(red: 0.2392156869, green: 0.6745098233, blue: 0.9686274529, alpha: 1))
        buyDrillText.center.y = 14
        buyDrillText.center.x -= 21
        
        var buyAutoDrillText = Text(string: "Buy auto drill", fontSize: 51.0, fontName: "Copperplate", color: #colorLiteral(red: 0.2392156869, green: 0.6745098233, blue: 0.9686274529, alpha: 1))
        buyAutoDrillText.center.y = 14
        buyAutoDrillText.center.x = 15
        
        backText.onTouchUp {
            defaults.set(drillInfo, forKey: localStorage.drillInfoKey)
            defaults.set(currentGemType, forKey: localStorage.currentGemTypeKey)
            defaults.set(nextGemType, forKey: localStorage.nextGemTypeKey)
            primary()
        }
    }
    
    func primary() {
        Canvas.shared.clear()
        
        Canvas.shared.color = Color.black
        var gem = Image(name: String(currentGemType["image"] ?? currentGemTypeDefault["image"]!))
        gem.size.width = 60
        gem.size.height = 60
        gem.center.x = 0
        gem.center.y -= 10
        
        var gemsText = Text(string: "Gems: " + String(gems), fontSize: 70.0, fontName: "Copperplate", color: #colorLiteral(red: 0.2392156869, green: 0.6745098233, blue: 0.9686274529, alpha: 1))
        gemsText.center.y = 30
        gemsText.center.x = 0
        
        let storeText = Text(string: "Store", fontSize: 50.0, fontName: "Copperplate", color: #colorLiteral(red: 0.2392156869, green: 0.6745098233, blue: 0.9686274529, alpha: 1))
        storeText.center.y = 38
        storeText.center.x = 25
        
        storeText.onTouchUp {
            store()
        }
        
        gem.onTouchDown {
            gems += 1
            gemsText.string = "Gems: " + String(gems)
            defaults.set(gems, forKey: localStorage.gemsKey)

        }
    }
    primary()
}

class ViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
        self.view = Canvas.shared.backingView
        startup()
        main()
    }

}
