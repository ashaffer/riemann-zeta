import RHBridge.P2RoundedFactorCheckpointData11

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel11FactorChunk13 :
    P2RoundedFactorCheckpointData.panel11Prefix52 =
      normalizedPrefixTermAtomApprox ⟨52, by decide⟩ ⟨11, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel11Prefix53 =
      normalizedPrefixTermAtomApprox ⟨53, by decide⟩ ⟨11, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel11Prefix54 =
      normalizedPrefixTermAtomApprox ⟨54, by decide⟩ ⟨11, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel11Prefix55 =
      normalizedPrefixTermAtomApprox ⟨55, by decide⟩ ⟨11, by decide⟩ := by
  decide +kernel

theorem panel11Prefix52_eq :
    P2RoundedFactorCheckpointData.panel11Prefix52 =
      normalizedPrefixTermAtomApprox ⟨52, by decide⟩ ⟨11, by decide⟩ := by
  exact panel11FactorChunk13.1

theorem panel11Prefix53_eq :
    P2RoundedFactorCheckpointData.panel11Prefix53 =
      normalizedPrefixTermAtomApprox ⟨53, by decide⟩ ⟨11, by decide⟩ := by
  exact panel11FactorChunk13.2.1

theorem panel11Prefix54_eq :
    P2RoundedFactorCheckpointData.panel11Prefix54 =
      normalizedPrefixTermAtomApprox ⟨54, by decide⟩ ⟨11, by decide⟩ := by
  exact panel11FactorChunk13.2.2.1

theorem panel11Prefix55_eq :
    P2RoundedFactorCheckpointData.panel11Prefix55 =
      normalizedPrefixTermAtomApprox ⟨55, by decide⟩ ⟨11, by decide⟩ := by
  exact panel11FactorChunk13.2.2.2

end RHP2Bridge
