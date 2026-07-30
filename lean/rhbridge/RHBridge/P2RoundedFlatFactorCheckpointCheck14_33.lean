import RHBridge.P2RoundedFlatFactorCheckpointData14

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel14FlatComponentChunk33 :
    P2RoundedFactorCheckpointData.panel14FlatOdd9 =
      (P2RoundedFactorCheckpointData.panel14TruncatedOddComponents).get ⟨9, by decide⟩ := by
  decide +kernel

theorem panel14FlatOdd9_eq :
    P2RoundedFactorCheckpointData.panel14FlatOdd9 =
      (P2RoundedFactorCheckpointData.panel14TruncatedOddComponents).get ⟨9, by decide⟩ := by
  exact panel14FlatComponentChunk33

end RHP2Bridge
