import RHBridge.P2RoundedFactorCheckpointData11

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel11FactorChunk15 :
    P2RoundedFactorCheckpointData.panel11Prefix60 =
      normalizedPrefixTermAtomApprox ⟨60, by decide⟩ ⟨11, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel11Prefix61 =
      normalizedPrefixTermAtomApprox ⟨61, by decide⟩ ⟨11, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel11Prefix62 =
      normalizedPrefixTermAtomApprox ⟨62, by decide⟩ ⟨11, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel11Prefix63 =
      normalizedPrefixTermAtomApprox ⟨63, by decide⟩ ⟨11, by decide⟩ := by
  decide +kernel

theorem panel11Prefix60_eq :
    P2RoundedFactorCheckpointData.panel11Prefix60 =
      normalizedPrefixTermAtomApprox ⟨60, by decide⟩ ⟨11, by decide⟩ := by
  exact panel11FactorChunk15.1

theorem panel11Prefix61_eq :
    P2RoundedFactorCheckpointData.panel11Prefix61 =
      normalizedPrefixTermAtomApprox ⟨61, by decide⟩ ⟨11, by decide⟩ := by
  exact panel11FactorChunk15.2.1

theorem panel11Prefix62_eq :
    P2RoundedFactorCheckpointData.panel11Prefix62 =
      normalizedPrefixTermAtomApprox ⟨62, by decide⟩ ⟨11, by decide⟩ := by
  exact panel11FactorChunk15.2.2.1

theorem panel11Prefix63_eq :
    P2RoundedFactorCheckpointData.panel11Prefix63 =
      normalizedPrefixTermAtomApprox ⟨63, by decide⟩ ⟨11, by decide⟩ := by
  exact panel11FactorChunk15.2.2.2

end RHP2Bridge
