import RHBridge.P2RoundedFactorCheckpointData24

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel24FactorChunk12 :
    P2RoundedFactorCheckpointData.panel24Prefix48 =
      normalizedPrefixTermAtomApprox ⟨48, by decide⟩ ⟨24, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel24Prefix49 =
      normalizedPrefixTermAtomApprox ⟨49, by decide⟩ ⟨24, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel24Prefix50 =
      normalizedPrefixTermAtomApprox ⟨50, by decide⟩ ⟨24, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel24Prefix51 =
      normalizedPrefixTermAtomApprox ⟨51, by decide⟩ ⟨24, by decide⟩ := by
  decide +kernel

theorem panel24Prefix48_eq :
    P2RoundedFactorCheckpointData.panel24Prefix48 =
      normalizedPrefixTermAtomApprox ⟨48, by decide⟩ ⟨24, by decide⟩ := by
  exact panel24FactorChunk12.1

theorem panel24Prefix49_eq :
    P2RoundedFactorCheckpointData.panel24Prefix49 =
      normalizedPrefixTermAtomApprox ⟨49, by decide⟩ ⟨24, by decide⟩ := by
  exact panel24FactorChunk12.2.1

theorem panel24Prefix50_eq :
    P2RoundedFactorCheckpointData.panel24Prefix50 =
      normalizedPrefixTermAtomApprox ⟨50, by decide⟩ ⟨24, by decide⟩ := by
  exact panel24FactorChunk12.2.2.1

theorem panel24Prefix51_eq :
    P2RoundedFactorCheckpointData.panel24Prefix51 =
      normalizedPrefixTermAtomApprox ⟨51, by decide⟩ ⟨24, by decide⟩ := by
  exact panel24FactorChunk12.2.2.2

end RHP2Bridge
