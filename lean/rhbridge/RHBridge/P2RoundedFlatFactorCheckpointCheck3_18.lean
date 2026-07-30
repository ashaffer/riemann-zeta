import RHBridge.P2RoundedFlatFactorCheckpointData3

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel3FlatComponentChunk18 :
    P2RoundedFactorCheckpointData.panel3FlatEven18 =
      (P2RoundedFactorCheckpointData.panel3TruncatedEvenComponents).get ⟨18, by decide⟩ := by
  decide +kernel

theorem panel3FlatEven18_eq :
    P2RoundedFactorCheckpointData.panel3FlatEven18 =
      (P2RoundedFactorCheckpointData.panel3TruncatedEvenComponents).get ⟨18, by decide⟩ := by
  exact panel3FlatComponentChunk18

end RHP2Bridge
