import RHBridge.P2RoundedFlatFactorCheckpointData31

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel31FlatComponentChunk18 :
    P2RoundedFactorCheckpointData.panel31FlatEven18 =
      (P2RoundedFactorCheckpointData.panel31TruncatedEvenComponents).get ⟨18, by decide⟩ := by
  decide +kernel

theorem panel31FlatEven18_eq :
    P2RoundedFactorCheckpointData.panel31FlatEven18 =
      (P2RoundedFactorCheckpointData.panel31TruncatedEvenComponents).get ⟨18, by decide⟩ := by
  exact panel31FlatComponentChunk18

end RHP2Bridge
