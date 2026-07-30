import RHBridge.P2RoundedFlatFactorCheckpointData31

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel31FlatComponentChunk6 :
    P2RoundedFactorCheckpointData.panel31FlatEven6 =
      (P2RoundedFactorCheckpointData.panel31TruncatedEvenComponents).get ⟨6, by decide⟩ := by
  decide +kernel

theorem panel31FlatEven6_eq :
    P2RoundedFactorCheckpointData.panel31FlatEven6 =
      (P2RoundedFactorCheckpointData.panel31TruncatedEvenComponents).get ⟨6, by decide⟩ := by
  exact panel31FlatComponentChunk6

end RHP2Bridge
