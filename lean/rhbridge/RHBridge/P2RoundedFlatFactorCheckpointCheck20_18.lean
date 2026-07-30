import RHBridge.P2RoundedFlatFactorCheckpointData20

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel20FlatComponentChunk18 :
    P2RoundedFactorCheckpointData.panel20FlatEven18 =
      (P2RoundedFactorCheckpointData.panel20TruncatedEvenComponents).get ⟨18, by decide⟩ := by
  decide +kernel

theorem panel20FlatEven18_eq :
    P2RoundedFactorCheckpointData.panel20FlatEven18 =
      (P2RoundedFactorCheckpointData.panel20TruncatedEvenComponents).get ⟨18, by decide⟩ := by
  exact panel20FlatComponentChunk18

end RHP2Bridge
