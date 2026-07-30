import RHBridge.P2RoundedFactorCheckpointData29

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel29FactorChunk13 :
    P2RoundedFactorCheckpointData.panel29Prefix52 =
      normalizedPrefixTermAtomApprox ⟨52, by decide⟩ ⟨29, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel29Prefix53 =
      normalizedPrefixTermAtomApprox ⟨53, by decide⟩ ⟨29, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel29Prefix54 =
      normalizedPrefixTermAtomApprox ⟨54, by decide⟩ ⟨29, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel29Prefix55 =
      normalizedPrefixTermAtomApprox ⟨55, by decide⟩ ⟨29, by decide⟩ := by
  decide +kernel

theorem panel29Prefix52_eq :
    P2RoundedFactorCheckpointData.panel29Prefix52 =
      normalizedPrefixTermAtomApprox ⟨52, by decide⟩ ⟨29, by decide⟩ := by
  exact panel29FactorChunk13.1

theorem panel29Prefix53_eq :
    P2RoundedFactorCheckpointData.panel29Prefix53 =
      normalizedPrefixTermAtomApprox ⟨53, by decide⟩ ⟨29, by decide⟩ := by
  exact panel29FactorChunk13.2.1

theorem panel29Prefix54_eq :
    P2RoundedFactorCheckpointData.panel29Prefix54 =
      normalizedPrefixTermAtomApprox ⟨54, by decide⟩ ⟨29, by decide⟩ := by
  exact panel29FactorChunk13.2.2.1

theorem panel29Prefix55_eq :
    P2RoundedFactorCheckpointData.panel29Prefix55 =
      normalizedPrefixTermAtomApprox ⟨55, by decide⟩ ⟨29, by decide⟩ := by
  exact panel29FactorChunk13.2.2.2

end RHP2Bridge
