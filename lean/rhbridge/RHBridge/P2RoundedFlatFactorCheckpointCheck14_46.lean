import RHBridge.P2RoundedFlatFactorCheckpointData14

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel14FlatComponentChunk46 :
    P2RoundedFactorCheckpointData.panel14FlatOdd22 =
      (P2RoundedFactorCheckpointData.panel14TruncatedOddComponents).get ⟨22, by decide⟩ := by
  decide +kernel

theorem panel14FlatOdd22_eq :
    P2RoundedFactorCheckpointData.panel14FlatOdd22 =
      (P2RoundedFactorCheckpointData.panel14TruncatedOddComponents).get ⟨22, by decide⟩ := by
  exact panel14FlatComponentChunk46

end RHP2Bridge
