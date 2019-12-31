//
//  ViewController.swift
//  Catapult

import UIKit

class ViewController: UIViewController {
    
    // the first screen
    func startscreen() {
        Canvas.shared.clear()
        Canvas.shared.color = .black
        let playgroundText = Text(string: "Playground", fontSize: 32.0, fontName: "Copperplate", color: #colorLiteral(red: 0, green: 0.7262907624, blue: 0.8682622313, alpha: 1))
        
        playgroundText.onTouchUp {
            self.playground()
        }
    }
    
    // freeplay mode
    func playground() {
        Canvas.shared.clear()
        // changing background color
        Canvas.shared.color = .white
        
        // tries
        var tries = 0
        // checks if projectile is running
        var isRunning = 0
        // the score!
        var score = 0
        // the projectile
        var proj = Circle(radius: 0)
        
        // back text
        let backText = Text(string: "Back", fontSize: 32.0, fontName: "Copperplate", color: #colorLiteral(red: 0.09019608050584793, green: 0.0, blue: 0.3019607961177826, alpha: 1.0))
        backText.center.y = 30
        backText.center.x = -37
        
        // tries text
        var triesText = Text(string: "Tries: " + String(tries), fontSize: 32.0, fontName: "Copperplate", color: #colorLiteral(red: 0.09019608050584793, green: 0.0, blue: 0.3019607961177826, alpha: 1.0))
        triesText.center.y = 25
        triesText.center.x = -17
        
        // score text
        var scoreText = Text(string: "Score: " + String(score), fontSize: 32.0, fontName: "Copperplate", color: #colorLiteral(red: 0.09019608050584793, green: 0.0, blue: 0.3019607961177826, alpha: 1.0))
        scoreText.center.y = 25
        scoreText.center.x = 16
        
        // store text
        // var storeText = Text(string: "Store", fontSize: 32.0, fontName: "Courier New", color: #colorLiteral(red: 0.1411764771, green: 0.3960784376, blue: 0.5647059083, alpha: 1))
        // storeText.center.y = 31
        // storeText.center.x = 30
        
        // line connecting the basket to the catapult
        var line = Line(start: Point(x: -18, y: -11), end: Point(x: -13, y: -19), thickness: 0.5)
        line.color = .gray
        
        // the target! (bulls eye)
        let target = Rectangle()
        target.color = .red
        target.size.width = 3
        target.size.height = 6
        target.center.x = 18
        
        // importing picture of catapult into playgrounds
        let catapult = Image(name: "Catapult2.png")
        catapult.size.width = 50
        catapult.size.height = 50
        catapult.center.y -= 15
        catapult.center.x -= 15
        
        // the basket
        let basket = Image(name: "Basket Head 3.png")
        basket.size.width = 6.5
        basket.size.height = 6.5
        basket.center.x -= 18
        basket.center.y -= 11
        basket.draggable = true
        
        // getting back to the first screen
        backText.onTouchUp {
            self.startscreen()
        }
        
        // not letting the basket get too far away
        basket.onTouchDrag {
            if basket.center.x >= -18 {
                basket.center.x = -18
            }
            
            if basket.center.y >= -11 {
                basket.center.y = -11
            }
            
            if basket.center.x <= -21 {
                basket.center.x = -21
            }
            
            if basket.center.y <= -17 {
                basket.center.y = -17
            }
            
            // using Pythogaros Theorem to keep basket same distance from
            // catapult at all times
            basket.center.x = -11 - sqrt(89.0 - pow(-17.0 - basket.center.y, 2))
            line.start = Point(x: basket.center.x, y: basket.center.y)
        }
        
        // shooting the catapult!
        func proj_move(range: Double) {
            
            // not letting the function run if one projectile is shooting
            if isRunning != 0 {
                return
            }
            isRunning = 1
            
            // making projectile
            proj = Circle(radius: 1.3)
            proj.color = Color.black
            proj.center.x -= 18
            proj.center.y -= 11
            proj.draggable = false
            
            // moving the projectile
            UIView.animateKeyframes(withDuration: 3, delay: 0, animations: {
                
                // for every step move a little bit
                for x in 0 ... 9 {
                    UIView.addKeyframe(withRelativeStartTime: Double(x)/10, relativeDuration: 0.1) {
                        
                        // parabola calculations
                        proj.center.x += 36.0 / 10.0
                        proj.center.y = -11 + ((4.0 + Double(range)) * Double(x+1)) - (0.5 * 1.4 * pow(Double(x+1), 2))
                        
                        // shrink the projectile out of existence
                        if x == 9 {
                            tries += 1
                            triesText.string = "Tries: " + String(tries)
                            
                            Timer.scheduledTimer(withTimeInterval: 3.0, repeats: false) { timer in
                                animate(duration: 3) {
                                    proj.radius = 0
                                }
                                
                                // let catapult shoot for another time
                                isRunning = 0
                            }
                        }
                    }
                }
                
                // the target calculations
                if target.center.y+3 >= proj.center.y
                    && target.center.y-3 <= proj.center.y
                    && abs(target.center.x - proj.center.x) < 0.001 {
                    // projectile has hit the target
                    score += 10
                    
                    // add score to the text
                    Timer.scheduledTimer(withTimeInterval: 3.0, repeats: false) { timer in
                        animate(duration: 1.5) {
                            scoreText.string = "Score: " + String(score)
                            
                            // make the target jump to a random y between two numbers
                            target.center.y = Double(arc4random_uniform(19 + 23)) - 23.0
                        }
                    }
                }
            }
            )
        }
        
        // when you let go of the basket
        basket.onTouchUp {
            if (basket.center.x != -18) && (basket.center.y != -11) {
                // shoot the projectile
                proj_move(range: -11 - basket.center.y)
                // move basket back to home
                animate() {
                    basket.center.x = -18
                    basket.center.y = -11
                    line.start = Point(x: basket.center.x, y: basket.center.y)
                }
            }
        }
        
        // easter eggs
        scoreText.onTouchDown {
            Canvas.shared.color = #colorLiteral(red: 0.9098039269447327, green: 0.47843137383461, blue: 0.6431372761726379, alpha: 1.0)
        }
        target.onTouchDown {
            target.color = .random()
        }
        triesText.onTouchDown {
            Canvas.shared.color = .random()
        }
        catapult.onTouchDown {
            Canvas.shared.color = .white
        }
        
        // storeText.onTouchUp {
        // }

    }

    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
        self.view = Canvas.shared.backingView
        self.preferredContentSize = CGSize(width: UIScreen.main.bounds.width, height: UIScreen.main.bounds.height)
        Canvas.shared.numPointsPerUnit = Double(UIScreen.main.bounds.height * 0.014)
        startscreen()
    }

}

