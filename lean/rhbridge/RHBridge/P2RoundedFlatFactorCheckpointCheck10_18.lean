import RHBridge.P2RoundedFlatFactorCheckpointData10

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel10FlatComponentChunk18 :
    P2RoundedFactorCheckpointData.panel10FlatEven18 =
      (P2RoundedFactorCheckpointData.panel10TruncatedEvenComponents).get ⟨18, by decide⟩ := by
  decide +kernel

theorem panel10FlatEven18_eq :
    P2RoundedFactorCheckpointData.panel10FlatEven18 =
      (P2RoundedFactorCheckpointData.panel10TruncatedEvenComponents).get ⟨18, by decide⟩ := by
  exact panel10FlatComponentChunk18

end RHP2Bridge
