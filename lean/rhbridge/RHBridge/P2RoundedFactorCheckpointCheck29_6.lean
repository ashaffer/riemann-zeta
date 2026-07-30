import RHBridge.P2RoundedFactorCheckpointData29

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel29FactorChunk6 :
    P2RoundedFactorCheckpointData.panel29Prefix24 =
      normalizedPrefixTermAtomApprox ⟨24, by decide⟩ ⟨29, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel29Prefix25 =
      normalizedPrefixTermAtomApprox ⟨25, by decide⟩ ⟨29, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel29Prefix26 =
      normalizedPrefixTermAtomApprox ⟨26, by decide⟩ ⟨29, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel29Prefix27 =
      normalizedPrefixTermAtomApprox ⟨27, by decide⟩ ⟨29, by decide⟩ := by
  decide +kernel

theorem panel29Prefix24_eq :
    P2RoundedFactorCheckpointData.panel29Prefix24 =
      normalizedPrefixTermAtomApprox ⟨24, by decide⟩ ⟨29, by decide⟩ := by
  exact panel29FactorChunk6.1

theorem panel29Prefix25_eq :
    P2RoundedFactorCheckpointData.panel29Prefix25 =
      normalizedPrefixTermAtomApprox ⟨25, by decide⟩ ⟨29, by decide⟩ := by
  exact panel29FactorChunk6.2.1

theorem panel29Prefix26_eq :
    P2RoundedFactorCheckpointData.panel29Prefix26 =
      normalizedPrefixTermAtomApprox ⟨26, by decide⟩ ⟨29, by decide⟩ := by
  exact panel29FactorChunk6.2.2.1

theorem panel29Prefix27_eq :
    P2RoundedFactorCheckpointData.panel29Prefix27 =
      normalizedPrefixTermAtomApprox ⟨27, by decide⟩ ⟨29, by decide⟩ := by
  exact panel29FactorChunk6.2.2.2

end RHP2Bridge
