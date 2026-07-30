import RHBridge.P2RoundedFlatFactorCheckpointData14

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel14FlatComponentChunk35 :
    P2RoundedFactorCheckpointData.panel14FlatOdd11 =
      (P2RoundedFactorCheckpointData.panel14TruncatedOddComponents).get ⟨11, by decide⟩ := by
  decide +kernel

theorem panel14FlatOdd11_eq :
    P2RoundedFactorCheckpointData.panel14FlatOdd11 =
      (P2RoundedFactorCheckpointData.panel14TruncatedOddComponents).get ⟨11, by decide⟩ := by
  exact panel14FlatComponentChunk35

end RHP2Bridge
