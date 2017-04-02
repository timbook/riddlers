findAngle <- function(l1, inner, l2) {
  A <- l1 - inner
  B <- l2 - inner
  theta <- acos(sum(A * B) / (norm(A, '2') * norm(B, '2')))
  return(theta)
}

is_convex <- function(p1, p2, p3, p4) {
  ### Determine if reflex at each point.
  # Point I
  theta1 <- findAngle(p2, p1, p3)
  theta2 <- findAngle(p3, p1, p4)
  if (theta1 + theta2 > pi) return(FALSE)
  
  # Point II
  theta1 <- findAngle(p3, p2, p4)
  theta2 <- findAngle(p4, p2, p1)
  if (theta1 + theta2 > pi) return(FALSE)
  
  # Point III
  theta1 <- findAngle(p2, p3, p1)
  theta2 <- findAngle(p1, p3, p4)
  if (theta1 + theta2 > pi) return(FALSE)
  
  # Point IV
  theta1 <- findAngle(p1, p4, p2)
  theta2 <- findAngle(p2, p4, p3)
  if (theta1 + theta2 > pi) return(FALSE)
  
  return(TRUE)
}

