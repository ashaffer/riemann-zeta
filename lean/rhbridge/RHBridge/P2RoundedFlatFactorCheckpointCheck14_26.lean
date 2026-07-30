import RHBridge.P2RoundedFlatFactorCheckpointData14

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel14FlatComponentChunk26 :
    P2RoundedFactorCheckpointData.panel14FlatOdd2 =
      (P2RoundedFactorCheckpointData.panel14TruncatedOddComponents).get ⟨2, by decide⟩ := by
  decide +kernel

theorem panel14FlatOdd2_eq :
    P2RoundedFactorCheckpointData.panel14FlatOdd2 =
      (P2RoundedFactorCheckpointData.panel14TruncatedOddComponents).get ⟨2, by decide⟩ := by
  exact panel14FlatComponentChunk26

end RHP2Bridge
