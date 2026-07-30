import RHBridge.P2RoundedFlatFactorCheckpointData14

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel14FlatComponentChunk41 :
    P2RoundedFactorCheckpointData.panel14FlatOdd17 =
      (P2RoundedFactorCheckpointData.panel14TruncatedOddComponents).get ⟨17, by decide⟩ := by
  decide +kernel

theorem panel14FlatOdd17_eq :
    P2RoundedFactorCheckpointData.panel14FlatOdd17 =
      (P2RoundedFactorCheckpointData.panel14TruncatedOddComponents).get ⟨17, by decide⟩ := by
  exact panel14FlatComponentChunk41

end RHP2Bridge
