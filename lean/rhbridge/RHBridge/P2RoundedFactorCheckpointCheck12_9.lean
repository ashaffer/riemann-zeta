import RHBridge.P2RoundedFactorCheckpointData12

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel12FactorChunk9 :
    P2RoundedFactorCheckpointData.panel12Prefix36 =
      normalizedPrefixTermAtomApprox ⟨36, by decide⟩ ⟨12, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel12Prefix37 =
      normalizedPrefixTermAtomApprox ⟨37, by decide⟩ ⟨12, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel12Prefix38 =
      normalizedPrefixTermAtomApprox ⟨38, by decide⟩ ⟨12, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel12Prefix39 =
      normalizedPrefixTermAtomApprox ⟨39, by decide⟩ ⟨12, by decide⟩ := by
  decide +kernel

theorem panel12Prefix36_eq :
    P2RoundedFactorCheckpointData.panel12Prefix36 =
      normalizedPrefixTermAtomApprox ⟨36, by decide⟩ ⟨12, by decide⟩ := by
  exact panel12FactorChunk9.1

theorem panel12Prefix37_eq :
    P2RoundedFactorCheckpointData.panel12Prefix37 =
      normalizedPrefixTermAtomApprox ⟨37, by decide⟩ ⟨12, by decide⟩ := by
  exact panel12FactorChunk9.2.1

theorem panel12Prefix38_eq :
    P2RoundedFactorCheckpointData.panel12Prefix38 =
      normalizedPrefixTermAtomApprox ⟨38, by decide⟩ ⟨12, by decide⟩ := by
  exact panel12FactorChunk9.2.2.1

theorem panel12Prefix39_eq :
    P2RoundedFactorCheckpointData.panel12Prefix39 =
      normalizedPrefixTermAtomApprox ⟨39, by decide⟩ ⟨12, by decide⟩ := by
  exact panel12FactorChunk9.2.2.2

end RHP2Bridge
