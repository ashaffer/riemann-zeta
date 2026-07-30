import RHBridge.P2RoundedFlatFactorCheckpointData14

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel14FlatComponentChunk43 :
    P2RoundedFactorCheckpointData.panel14FlatOdd19 =
      (P2RoundedFactorCheckpointData.panel14TruncatedOddComponents).get ⟨19, by decide⟩ := by
  decide +kernel

theorem panel14FlatOdd19_eq :
    P2RoundedFactorCheckpointData.panel14FlatOdd19 =
      (P2RoundedFactorCheckpointData.panel14TruncatedOddComponents).get ⟨19, by decide⟩ := by
  exact panel14FlatComponentChunk43

end RHP2Bridge
