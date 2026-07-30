import RHBridge.P2RoundedFlatFactorCheckpointData27

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel27FlatComponentChunk18 :
    P2RoundedFactorCheckpointData.panel27FlatEven18 =
      (P2RoundedFactorCheckpointData.panel27TruncatedEvenComponents).get ⟨18, by decide⟩ := by
  decide +kernel

theorem panel27FlatEven18_eq :
    P2RoundedFactorCheckpointData.panel27FlatEven18 =
      (P2RoundedFactorCheckpointData.panel27TruncatedEvenComponents).get ⟨18, by decide⟩ := by
  exact panel27FlatComponentChunk18

end RHP2Bridge
