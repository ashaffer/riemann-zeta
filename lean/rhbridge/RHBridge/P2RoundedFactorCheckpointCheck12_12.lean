import RHBridge.P2RoundedFactorCheckpointData12

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel12FactorChunk12 :
    P2RoundedFactorCheckpointData.panel12Prefix48 =
      normalizedPrefixTermAtomApprox ⟨48, by decide⟩ ⟨12, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel12Prefix49 =
      normalizedPrefixTermAtomApprox ⟨49, by decide⟩ ⟨12, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel12Prefix50 =
      normalizedPrefixTermAtomApprox ⟨50, by decide⟩ ⟨12, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel12Prefix51 =
      normalizedPrefixTermAtomApprox ⟨51, by decide⟩ ⟨12, by decide⟩ := by
  decide +kernel

theorem panel12Prefix48_eq :
    P2RoundedFactorCheckpointData.panel12Prefix48 =
      normalizedPrefixTermAtomApprox ⟨48, by decide⟩ ⟨12, by decide⟩ := by
  exact panel12FactorChunk12.1

theorem panel12Prefix49_eq :
    P2RoundedFactorCheckpointData.panel12Prefix49 =
      normalizedPrefixTermAtomApprox ⟨49, by decide⟩ ⟨12, by decide⟩ := by
  exact panel12FactorChunk12.2.1

theorem panel12Prefix50_eq :
    P2RoundedFactorCheckpointData.panel12Prefix50 =
      normalizedPrefixTermAtomApprox ⟨50, by decide⟩ ⟨12, by decide⟩ := by
  exact panel12FactorChunk12.2.2.1

theorem panel12Prefix51_eq :
    P2RoundedFactorCheckpointData.panel12Prefix51 =
      normalizedPrefixTermAtomApprox ⟨51, by decide⟩ ⟨12, by decide⟩ := by
  exact panel12FactorChunk12.2.2.2

end RHP2Bridge
