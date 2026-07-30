import RHBridge.P2RoundedFlatFactorCheckpointData12

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel12FlatComponentChunk18 :
    P2RoundedFactorCheckpointData.panel12FlatEven18 =
      (P2RoundedFactorCheckpointData.panel12TruncatedEvenComponents).get ⟨18, by decide⟩ := by
  decide +kernel

theorem panel12FlatEven18_eq :
    P2RoundedFactorCheckpointData.panel12FlatEven18 =
      (P2RoundedFactorCheckpointData.panel12TruncatedEvenComponents).get ⟨18, by decide⟩ := by
  exact panel12FlatComponentChunk18

end RHP2Bridge
