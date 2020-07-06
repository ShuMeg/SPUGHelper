(define (problem Hum_Control)
   (:domain group25)
   (:objects dhr hr TargetH CurrentH)
   (:init 
          (DeHum_fr dhr)
          (Hum_fr hr)
          (Humidity TargetH)
          (Humidity CurrentH)
          (inRange CurrentH TargetH)
          (isON dhr)
          (isON hr)
          )
   (:goal (and(iSOFF dhr)
              (isOFF hr)))
              )