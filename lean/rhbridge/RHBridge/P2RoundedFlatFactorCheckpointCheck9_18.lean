import RHBridge.P2RoundedFlatFactorCheckpointData9

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel9FlatComponentChunk18 :
    P2RoundedFactorCheckpointData.panel9FlatEven18 =
      (P2RoundedFactorCheckpointData.panel9TruncatedEvenComponents).get ⟨18, by decide⟩ := by
  decide +kernel

theorem panel9FlatEven18_eq :
    P2RoundedFactorCheckpointData.panel9FlatEven18 =
      (P2RoundedFactorCheckpointData.panel9TruncatedEvenComponents).get ⟨18, by decide⟩ := by
  exact panel9FlatComponentChunk18

end RHP2Bridge
