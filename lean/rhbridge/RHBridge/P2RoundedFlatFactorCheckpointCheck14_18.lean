import RHBridge.P2RoundedFlatFactorCheckpointData14

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel14FlatComponentChunk18 :
    P2RoundedFactorCheckpointData.panel14FlatEven18 =
      (P2RoundedFactorCheckpointData.panel14TruncatedEvenComponents).get ⟨18, by decide⟩ := by
  decide +kernel

theorem panel14FlatEven18_eq :
    P2RoundedFactorCheckpointData.panel14FlatEven18 =
      (P2RoundedFactorCheckpointData.panel14TruncatedEvenComponents).get ⟨18, by decide⟩ := by
  exact panel14FlatComponentChunk18

end RHP2Bridge
