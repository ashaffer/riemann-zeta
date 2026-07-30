import RHBridge.P2RoundedFlatFactorCheckpointData7

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel7FlatComponentChunk41 :
    P2RoundedFactorCheckpointData.panel7FlatOdd17 =
      (P2RoundedFactorCheckpointData.panel7TruncatedOddComponents).get ⟨17, by decide⟩ := by
  decide +kernel

theorem panel7FlatOdd17_eq :
    P2RoundedFactorCheckpointData.panel7FlatOdd17 =
      (P2RoundedFactorCheckpointData.panel7TruncatedOddComponents).get ⟨17, by decide⟩ := by
  exact panel7FlatComponentChunk41

end RHP2Bridge
